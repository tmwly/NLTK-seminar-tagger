import data_importer
from ontology_calc import Ontology_calc
import pos_tagger
from collections import Counter
from Ontology import Ontology

# train

pos_tagger = pos_tagger.train()

tagged_emails = data_importer.import_tagged_emails("seminars/seminar_testdata/test_tagged/")

training_tags = data_importer.import_training_emails("seminars/seminars_training/training/")

locations = training_tags[0]
speakers = training_tags[1]

# tag emails

untagged_emails = data_importer.import_emails("seminars/seminars_untagged/untagged/")

for email in untagged_emails:
    values = email.process(pos_tagger)

    if values[0] is not None:
        speakers.append(values[0])
    if values[1] is not None:
        locations.append(values[1])

locations = set(locations)
speakers = set(speakers)

for email in untagged_emails:
    if email.place is None:
        email.tag_location_list(locations)
    if email.who is None:
        email.tag_speakers_list(speakers)
    email.export()

# generate metrics
tp_classified = 0
num_classified = 0
tp_in_corpus = 0

for index, email in enumerate(tagged_emails):
    new_tags = untagged_emails[index].get_all_tags()
    training_tags = email.all_tags

    c1 = Counter([x[0] for x in new_tags])
    c2 = Counter([x[0] for x in training_tags])

    diff = c1 - c2

    tp = len(new_tags) - len(diff)

    tp_classified += tp

    # precision
    num_classified += len(new_tags)

    # recall
    tp_in_corpus += len(training_tags)


precision = float(tp_classified) / num_classified
recall = float(tp_classified) / tp_in_corpus

f_value = (2 * (precision * recall) / (precision + recall))

print "Precision: " + precision.__str__()
print "Recall: " + recall.__str__()
print "F value: " + f_value.__str__()


# ontology


common_words = ["a", "an", "about", "all", "also", "and", "as", "at", "be", "because", "but", "by", "can", "come",
                "could", "day", "do", "even", "find", "first", "for", "from", "get", "give", "go", "have", "he", "her",
                "here", "him", "his", "how", "i", "if", "in", "is", "into", "it", "its", "just", "know", "like", "look",
                "make", "man", "many", "me", "more", "my", "new", "no", "not", "now", "of", "on", "one", "only", "or",
                "other", "our", "out", "people", "say", "see", "she", "so", "some", "take", "tell", "than", "that",
                "the", "their", "them", "then", "there", "these", "they", "thing", "think", "this", "those", "time",
                "to", "two", "up", "use", "very", "want", "way", "we", "well", "what", "when", "which", "who", "will",
                "with", "would", "year", "you", "your", "lecture", "seminar", ",", "(", ")", ":", ".", "@", "--", "''",
                "!", "?", "|", "-", "]", "[", ">", "<", "*", "_", "``", "...", "talk", "undergrad"]

ontology = Ontology()

ontology_calc = Ontology_calc()
ontology_dict = ontology.traversal_info

for email in untagged_emails:
    word_freq = email.get_frequencies(common_words)

    topics = ontology_calc.find_closest_stripped(ontology_dict, word_freq)

    topic = topics[0][0]

    ontology.add_email(topic, email.name)

ont_string = ontology.__str__()
print ont_string

f = open("ontology.txt", "w+")

f.write(ont_string)
f.close()