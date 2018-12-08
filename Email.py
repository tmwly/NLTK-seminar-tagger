import corpus_generator
import os
import re
from nltk.corpus import names
from nltk.tokenize import sent_tokenize
from nltk.stem.porter import *


class Email:

    def __init__(self, name, head, type, who, topic, dates, time, place, duration, host, poster, abstract):
        self.name = name
        self.head = head
        self.type = type
        self.who = who
        self.topic = topic
        self.dates = dates
        self.time = time
        self.place = place
        self.duration = duration
        self.host = host
        self.poster = poster
        self.abstract = abstract
        self.tags = []
        self.head_tags = []
        self.pos = []
        self.tokens = self.get_tokens()

    def __str__(self):
        s = self.head + \
            '\nType:' + self.type

        if self.who is not None:
            s += '\nWho:' + self.who

        s += '\nTopic:' + self.topic + \
             '\nDates:' + self.dates + \
             '\nTime:' + self.time

        if self.place is not None:
            s += '\nPlace:' + self.place

        if self.duration is not None:
            s += '\nDuration:' + self.duration

        if self.host is not None:
            s += '\nHost:' + self.host

        s += '\nPostedBy:' + self.poster + \
             '\nAbstract:' + self.abstract

        return s

    def get_frequencies(self, common):
        stemmer = PorterStemmer()

        freq = {}
        for word in self.pos:
            string = stemmer.stem(word[0].lower())

            if string not in common:

                if string not in freq:
                    freq[string] = 1
                else:
                    freq[string] += 1

        sorted_dict = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_dict

    def get_tokens(self):
        tokens = corpus_generator.generate_tokens_single(self.abstract)
        return tokens

    def get_all_tags(self):
        tags = self.tags + self.head_tags
        return tags

    def process(self, tagger):

        self.pos = tagger.tag(self.tokens)
        # tag paragraphs and sentences first to not mess with other tags when outputting
        self.tag_paragraphs()  # and sentences
        self.tag_times()

        speaker = self.tag_speakers()
        location = self.tag_location()

        return speaker, location

    def tag_location(self):
        if self.place is not None:
            # tag location in header
            whitespace = re.match(r'\A\s+', self.place).group(0)

            place = re.sub(r'\A\s+', '', self.place)

            # add to tags
            self.head_tags.append((place, "location"))

            s = whitespace + '<location>' + place + '</location'
            self.place = s

            # tag location in body
            regex = r'' + re.escape(place) + r''
            matches = re.findall(regex, self.abstract)

            for match in matches:
                self.tags.append((match, "location"))

            return place

        return None

    def tag_location_list(self, locations):

        for value in locations:
            regex = r'' + re.escape(value) + r''

            results = re.findall(regex, self.abstract)

            for result in results:
                self.tags.append((result, "location"))

        # TODO extra location getting
        matches = re.findall(r'(?<= in )[a-zA-Z0-9 ]*(?= at \d)', self.abstract)

        for match in matches:
            self.tags.append((match, "location"))

    def tag_speakers(self):

        if self.who is not None:
            # tag location in header

            # strip leading whitespace
            stripped = re.sub(r'\A\s+', '', self.who)

            speaker = re.match(r'^.*?(?= *[,\/])|^.*', stripped).group(0)

            # add to tags
            self.head_tags.append((speaker, "speaker"))
            regex = r'' + re.escape(speaker) + r''

            string = "<speaker>" + speaker + "</speaker>"

            s = re.sub(regex, string, self.who)
            self.who = s

            # tag location in body
            regex = r'' + re.escape(speaker) + r''
            matches = re.findall(regex, self.abstract)

            for match in matches:
                self.tags.append((match, "speaker"))

            return speaker

        return None

    def tag_speakers_list(self, speakers):

        matched_speakers = 0
        for value in speakers:
            regex = r'' + re.escape(value) + r''

            results = re.findall(regex, self.abstract)

            for result in results:
                self.tags.append((result, "speaker"))
                matched_speakers += 1

        #todo improve this
        if matched_speakers > 0:
            tagged = self.pos

            l = len(tagged)

            for index, word in enumerate(tagged):

                if index < (l - 1):
                    #todo make this better and use regex
                    if word[1] == u'NP' and tagged[index + 1][1] == u'NP':
                        self.tags.append(((word[0] + " " + tagged[index + 1][0]), "speaker"))
                    elif word[1] == u'NP' and tagged[index + 1][1] == "unseen":
                        if tagged[index + 1][0] in names.words():
                            self.tags.append(((word[0] + " " + tagged[index + 1][0]), "speaker"))
                    elif word[1] == "unseen" and tagged[index + 1][1] == u'NP':
                        if word[0] in names.words():
                            self.tags.append(((word[0] + " " + tagged[index + 1][0]), "speaker"))
                    elif word[1] == "unseen" and tagged[index + 1][1] == "unseen":
                        if word[0] in names.words() and tagged[index + 1][0] in names.words():
                            self.tags.append(((word[0] + " " + tagged[index + 1][0]), "speaker"))

    def tag_sentences(self, paragraph):

        sentences = sent_tokenize(paragraph)

        for value in sentences:

            self.tags.append((value, "sentence"))

    def tag_paragraphs(self):

        # this one is ok
        # (?<=(?:\n\n))[^ ]{2,}.*?(?=(?:\n\n))

        # this one is better
        # (?<=(?:\n\n))(?:[^-]).*?(?=\n\n)

        regex = re.findall(r'(?<=(?:\n\n))(?:[^-]).*?(?=\n\n)', self.abstract, re.DOTALL)

        for match in regex:
            self.tags.append((match, "paragraph"))

        # second loop as sentences need to be tagged after paragraphs
        for match in regex:
            self.tag_sentences(match)

    def tag_times(self):

        # tag header
        # tag time
        if self.time is not None:
            header_times = []

            # get leading whitespace
            s = re.match(r'\A\s+', self.time).group(0)

            # remove leading whitespace
            string = re.sub(r'\A\s+', '', self.time)

            # find times from text
            times = re.findall(r'\d{1,2}:\d{2} AM|\d{1,2}:\d{2} PM|\d{1,2}:\d{2}', string)

            if len(times) > 1:
                # add to tags
                self.head_tags.append((times[0], "stime"))
                self.head_tags.append((times[1], "etime"))
                # save for body times
                header_times.append(times[0])
                header_times.append(times[1])

                stime = '<stime>' + times[0] + '</stime'
                stime_regex = r'\b' + times[0] + r'\b'

                tagged = re.sub(stime_regex, stime, string)

                etime = '<etime>' + times[1] + '</etime'
                etime_regex = r'\b' + times[1] + r'\b'
                tagged_two = re.sub(etime_regex, etime, tagged)

                s += tagged_two

            else:
                # add to tags
                self.head_tags.append((times[0], "stime"))
                header_times.append(times[0])
                s += '<stime>' + times[0] + '</stime'

            self.time = s

        # tag abstract using data from header

        times = re.findall(r'\d{1,2}(?::\d{2})?.?(?i)(?:P|A)(?:\.M\.?|M)(?![a-zA-Z])|\d{1,2}:\d{2}', self.abstract)

        temp_header_times = []

        # strip header formatting
        for value in header_times:
            temp_header_times.append(re.sub(r'[ ]', "", value))

        header_times = temp_header_times

        for value in times:
            # strip formatting
            value_formatted = value.upper()
            # remove whitespace
            value_formatted = re.sub(r'\s', "", value_formatted)
            # remove dots
            value_formatted = re.sub(r'\.', "", value_formatted)

            # add hours
            if re.match(r'^\d{1,2}(?:P|A)(?:\.M\.?|M)$', value_formatted):
                int = re.match(r'\d{1,2}', value_formatted).group(0)

                regex = r'' + int + r''

                value_formatted = re.sub(regex, int + ":00", value_formatted)

            if len(header_times) > 1:

                if value_formatted == header_times[0]:
                    self.tags.append((value, "stime"))
                elif value_formatted == header_times[1]:
                    self.tags.append((value, "etime"))
            elif len(header_times) == 1:

                if value_formatted == header_times[0]:
                    self.tags.append((value, "stime"))

    def export(self):

        self.write_tags()

        if not os.path.exists("output/"):
            os.makedirs("output/")

        f = open("output/" + self.name, "w+")

        f.write(self.__str__())
        f.close()

    def write_tags(self):
        # TODO fix for multiple of the same tag double tagging

        tagset = set(self.tags)

        for value in tagset:
            regex = r'' + re.escape(value[0]) + r''

            tagged_sent = "<" + value[1] + ">" + value[0] + "</" + value[1] + ">"

            temp = re.sub(regex, tagged_sent, self.abstract)
            self.abstract = temp
