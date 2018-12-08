import Email

import re
from os import listdir
from os.path import isfile, join

import TaggedEmail


def import_emails(location):
    filename_array = [f for f in listdir(location) if isfile(join(location, f))]
    emails = []

    for name in filename_array:
        email = import_single_email(location, name)
        if email is not None:
            emails.append(email)

    print('Total Emails: ')
    print(len(emails))
    return emails


def import_tagged_emails(location):
    filename_array = [f for f in listdir(location) if isfile(join(location, f))]
    emails = []

    for name in filename_array:

        text = open(location + name)
        string = text.read()

        if len(string) > 1:
            email = TaggedEmail.TaggedEmail(name, string)

            emails.append(email)

    print('Total Tagged Emails: ')
    print(len(emails))

    return emails


def import_single_email(location, name):
    text = open(location + name)
    string = text.read()

    if len(string) > 1:

        p = re.compile(r'(?<=)(.*?)>')
        email_head = p.search(string).group(0)

        # following regex needs to be updated to skip whitespace
        p = re.compile(r'(?<=Type:)\s*([^\n\r]*)')
        email_type = p.search(string).group(0)

        email_who = None
        if re.search(r'\bWho\b', string):
            p = re.compile(r'(?<=Who:)[\S\s]*?(?=\sTopic:)')
            email_who = p.search(string).group(0)

        p = re.compile(r'(?<=Topic:)[\S\s]*?(?=\sDates:)')
        email_topic = p.search(string).group(0)

        p = re.compile(r'(?<=Dates:)\s*([^\n\r]*)')
        email_dates = p.search(string).group(0)

        p = re.compile(r'(?<=Time:)\s*([^\n\r]*)')
        email_time = p.search(string).group(0)

        # check if contains place
        email_place = None
        if re.search(r'\bPlace\b', string):
            p = re.compile(r'(?<=Place:)\s*([^\n\r]*)')
            email_place = p.search(string).group(0)

        # check if contains duration
        email_duration = None
        if re.search(r'\bDuration\b', string):
            p = re.compile(r'(?<=Duration:)\s*([^\n\r]*)')
            email_duration = p.search(string).group(0)

        # check if contains host
        email_host = None
        if re.search(r'\bHost\b', string):
            p = re.compile(r'(?<=Host:)\s*([^\n\r]*)')
            email_host = p.search(string).group(0)

        p = re.compile(r'(?<=PostedBy:)\s*([^\n\r]*)')
        email_poster = p.search(string).group(0)

        p = re.compile(r'(?<=Abstract:)(.|\s)*')
        email_abstract = p.search(string).group(0)

        email = Email.Email(name, email_head, email_type, email_who, email_topic, email_dates, email_time, email_place,
                            email_duration, email_host, email_poster, email_abstract)

        return email
    return None
