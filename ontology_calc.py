import warnings

from nltk import PorterStemmer

from Ontology import Ontology

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim


class Ontology_calc:

    def __init__(self):
        print "loading Word2Vec model"
        self.model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
        print "model loaded"

    def find_closest_stripped(self, ontology_dict, words):
        model = self.model

        key_pairs = ontology_dict

        key_values = {}

        word_count = 0

        for word in words:
            if word[0] in model.vocab:
                word_count += word[1]

        # loop through topics
        for key in key_pairs:

            topic_words = key_pairs[key][1]  # get topic words
            key_total = 0
            topic_word_count = 0

            for topic_word in topic_words:
                if topic_word in model.vocab:
                    topic_word_count += 1

            # loop through stemmed words in email
            for word in words:

                word_total = 0
                for topic_word in topic_words:

                    if topic_word in model.vocab and word[0] in model.vocab:

                        score = (model.similarity(word[0], topic_word) * word[1])
                        if score > 0.8:
                            word_total += score
                    elif topic_word == word[0]:
                        score = 1 * word[1]
                        word_total += score

                key_total += (word_total / topic_word_count)

            key_values[key] = key_total / word_count  # normalise value

        sorted_dict = sorted(key_values.items(), key=lambda kv: kv[1], reverse=True)

        return sorted_dict
