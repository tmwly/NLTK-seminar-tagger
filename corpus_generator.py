from nltk import word_tokenize


def generate(text):
    data_string = ''
    # TODO remove 20 limit, only added for speed
    for value in text[:20]:
        # value.abstract is the content of the email
        data_string += value.abstract + '\n'

    tokens = word_tokenize(data_string)

    return tokens
