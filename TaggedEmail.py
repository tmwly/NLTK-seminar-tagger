import re


class TaggedEmail:

    def __init__(self, name, content):
        self.name = name
        self.content = content

        self.startTimes = self.get_tagged("stime")
        self.endTimes = self.get_tagged("etime")
        self.speaker = self.get_tagged("speaker")
        self.location = self.get_tagged("location")
        self.sentences = self.get_tagged("sentence")
        self.paragraphs = self.get_tagged("paragraph")

        self.all_tags = self.startTimes + self.endTimes + self.speaker + self.location + self.paragraphs + self.sentences

    def get_tagged(self, pattern):
        regex = r'(?<=<' + pattern + r'>).*?(?=<\/' + pattern + r'>)'

        search = re.findall(regex, self.content, re.DOTALL)

        values = []

        for match in search:
            values.append((match, pattern))

            regex = r'<' + pattern + r'>' + re.escape(match) + r'<\/' + pattern + r'>'

            temp = re.sub(regex, match, self.content)

            self.content = temp

        return values
