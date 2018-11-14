
from nltk.corpus import treebank
from nltk.corpus import brown
from nltk.tag import UnigramTagger
from nltk.tag import BigramTagger
from nltk.tag import TrigramTagger
from nltk.tag import DefaultTagger


def backoff_tagger(train_sents, tagger_classes, backoff=None):
    for cls in tagger_classes:

        backoff = cls(train_sents, backoff=backoff)

    return backoff


def train():
    print('Training:')
    # treebank.tagged_sents()[:3500]
    train_sents = brown.tagged_sents()[:50000]
    test_sents = brown.tagged_sents()[50000:]

    tagger_classes = [UnigramTagger, BigramTagger, TrigramTagger]

    tagger = backoff_tagger(train_sents, tagger_classes, backoff=DefaultTagger('NN'))
    print('Finished training, tagger accuracy:')
    print(tagger.evaluate(test_sents))

    return tagger
