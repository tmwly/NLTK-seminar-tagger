from nltk import word_tokenize
from nltk.tokenize import sent_tokenize


def generate_tokens_single(text):
    tokens = word_tokenize(text)

    return tokens


def generate_sentences(text):
    sents = sent_tokenize(text)

    return sents
