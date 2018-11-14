import Email

import re
from os import listdir
from os.path import isfile, join


def import_emails(location):

    filename_array = [f for f in listdir(location) if isfile(join(location, f))]
    emails = []

    for row in filename_array:
        email = import_single_email(location + row)
        emails.append(email)

    print('Total Emails: ')
    print(len(emails))
    return emails


def import_single_email(name):
    text = open(name)
    string = text.read()
    # print(string)

    if len(string) > 1:

        p = re.compile(r'(?<=\<)(.*?)(?=\>)')
        email_head = p.search(string).group(0)

        # following regex needs to be updated to skip whitespace
        p = re.compile(r'(?<=Type:)\s*([^\n\r]*)')
        email_type = p.search(string).group(0)

        p = re.compile(r'(?<=Topic:)\s*([^\n\r]*)')
        email_topic = p.search(string).group(0)

        p = re.compile(r'(?<=Dates:)\s*([^\n\r]*)')
        email_dates = p.search(string).group(0)

        p = re.compile(r'(?<=Time:)\s*([^\n\r]*)')
        email_time = p.search(string).group(0)

        p = re.compile(r'(?<=PostedBy:)\s*([^\n\r]*)')
        email_poster = p.search(string).group(0)

        p = re.compile(r'(?<=Abstract:)(.|\s)*')
        email_abstract = p.search(string).group(0)

        email = Email.Email(email_head, email_type, email_topic, email_dates, email_time, email_poster, email_abstract)

        # print(email.__str__())

        return email
    return None

