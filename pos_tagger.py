from nltk.corpus import brown
from nltk.tag import UnigramTagger
from nltk.tag import BigramTagger
from nltk.tag import TrigramTagger
from nltk.tag import DefaultTagger
from pickle import dump
from pickle import load


def backoff_tagger(train_sents, tagger_classes, backoff=None):
    for cls in tagger_classes:
        backoff = cls(train_sents, backoff=backoff)

    return backoff


def train():
    try:
        input = open('tagger.pkl', 'rb')
        print("Found tagger")

        tagger = load(input)
        input.close()
    except IOError:
        print('Training:')

        train_sents = brown.tagged_sents()[:50000]
        test_sents = brown.tagged_sents()[50000:]

        tagger_classes = [UnigramTagger, BigramTagger, TrigramTagger]

        tagger = backoff_tagger(train_sents, tagger_classes, backoff=DefaultTagger('unseen'))
        print('Finished training, tagger accuracy:')
        print(tagger.evaluate(test_sents))

        output = open('tagger.pkl', 'wb')
        dump(tagger, output, -1)
        output

    return tagger
