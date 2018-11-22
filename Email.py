import corpus_generator
import os
import re


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
        self.tokens = self.get_corpus()

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

    def get_corpus(self):
        tokens = corpus_generator.generate_tokens_single(self.abstract)

        return tokens

    def tag_body(self, tagger):
        tagged = tagger.tag(self.tokens)

        return tagged

    def export(self):
        if not os.path.exists("output/"):
            os.makedirs("output/")

        f = open("output/" + self.name, "w+")

        f.write(self.__str__())
        f.close

    def tag_head(self):
        # tag time
        if self.time is not None:
            s = re.match(r'\A\s+', self.time).group(0)

            string = re.sub(r'\A\s+', '', self.time)

            times = re.findall(r'\d{1,2}:\d{2} AM|\d{1,2}:\d{2} PM|\d{1,2}:\d{2}', string)

            if len(times) > 1:
                stime = '<stime>' + times[0] + '</stime'
                stime_regex = r'\b' + times[0] + r'\b'

                tagged = re.sub(stime_regex, stime, string)

                etime = '<etime>' + times[1] + '</etime'
                etime_regex = r'\b' + times[1] + r'\b'
                tagged_two = re.sub(etime_regex, etime, tagged)

                s += tagged_two

            else:
                s += '<stime>' + times[0] + '</stime'

            self.time = s

        # tag place
        if self.place is not None:
            whitespace = re.match(r'\A\s+', self.place).group(0)

            place = re.sub(r'\A\s+', '', self.place)

            s = whitespace + '<location>' + place + '</location'
            self.place = s

    def tag_sentences(self):
        return None
