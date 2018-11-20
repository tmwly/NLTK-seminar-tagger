import data_importer
import pos_tagger

emails = data_importer.import_emails("seminars/seminars_untagged/untagged/")

#pos_tagger = pos_tagger.train()


for email in emails:
    # print(email.tag_body(pos_tagger))
    email.tag_head()
    email.export()





