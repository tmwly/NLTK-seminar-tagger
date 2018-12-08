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

    def find_closest(self, ontology_dict, words):
        model = self.model
        stemmer = PorterStemmer()

        key_pairs = ontology_dict

        key_values = {}

        # loop through topics
        for key in key_pairs:

            topic_words = key_pairs[key][1]  # get topic words
            normalise_counter = 0

            total = 0
            key_values[key] = 0

            # loop through stemmed words in email
            for word in words:
                # loop through each word in topic
                topic_normalise_counter = 1
                word_score = 0

                word_bool = False

                if word[0] in model.vocab:
                    word_bool = True
                    normalise_counter += (1 * word[1])

                for topic_word in topic_words:
                    # if the words are present in word2vec, calculate score
                    stem_topic_word = stemmer.stem(topic_word)

                    if stem_topic_word in model.vocab and word_bool:

                        score = (model.similarity(word[0], stem_topic_word) * word[1])

                        # if score >= 0.5:
                        word_score += score
                        if topic_normalise_counter != 1:
                            topic_normalise_counter += (1 * word[1])
                    # else:
                    #     if word[0] == stemmer.stem(stem_topic_word):
                    #         score = 1 * word[1]
                    #         word_score += score
                    #         if topic_normalise_counter != 1:
                    #             topic_normalise_counter += (1 * word[1])

                # divide total by number of topic words to normalise

                total += (word_score / topic_normalise_counter)

            key_values[key] = (total / normalise_counter)  # normalise value

        sorted_dict = sorted(key_values.items(), key=lambda kv: kv[1], reverse=True)

        return sorted_dict

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
                        word_total += score

                key_total += (word_total / topic_word_count)

            key_values[key] = key_total / word_count  # normalise value

        sorted_dict = sorted(key_values.items(), key=lambda kv: kv[1], reverse=True)

        return sorted_dict
