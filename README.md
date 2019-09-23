# NLTK-seminar-tagger
This was a university project that aimed to tag and classify the content of seminar emails.
Information such as the seminar time, its location, the speaker and its topic were tagged.

First, a part-of-sentence tagger was trained and tested on the list of all sentences in the emails.
This POS data was then used to assist with tagging the speaker and the location.

Date/time data was tagged using regex.

Finally, a dictionary of topics and items in each topics was generated using word2vec, calculating the distance of each email from each of the pre-chosen topics, and then categorizing them.
