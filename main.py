import data_importer
import pos_tagger
import corpus_generator

emails = data_importer.import_emails("seminars/seminars_untagged/untagged/")

tokens = corpus_generator.generate(emails)

pos_tagger = pos_tagger.train()

print(pos_tagger.tag(tokens))




