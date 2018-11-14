class Email:

    def __init__(self, head, type, topic, dates, time, poster, abstract):
        self.head = head
        self.type = type
        self.topic = topic
        self.dates = dates
        self.time = time
        self.poster = poster
        self.abstract = abstract

    def __str__(self):
        return 'Head: ' + self.head + \
               '\nType: ' + self.type + \
               '\nTopic: ' + self.topic + \
               '\nDates: ' + self.dates + \
               '\nTime: ' + self.time + \
               '\nPoster: ' + self.poster + \
               '\nAbstract: ' + self.abstract
