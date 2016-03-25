from __future__ import division
from nltk.corpus.reader import CategorizedPlaintextCorpusReader
from nltk import FreqDist
from nltk.corpus import stopwords
import pandas as pd
import re

# define functions
def create_document_properties(cat, doc):
    words = [clean_string(x) for x in corpus.words(fileids=doc) if clean_string(x)!='']
    tot_words = len(words)
    sentences = len(corpus.sents(fileids=doc))
    word_sent = [len(x) for x in corpus.sents(doc)]
    avg_word = sum(word_sent)/len(word_sent)
    char_word = [len(x) for x in words]
    avg_char = sum(char_word)/len(char_word)
    words_ex_stop = [x for x in words if x not in stop]
    freq_dist = FreqDist(words_ex_stop)
    common = freq_dist.most_common(5)
    return (
        {
            "category": cat, "doc": doc,
            "tot_words": tot_words, "avg_char": avg_char,
            "sentences": sentences, "avg_word": avg_word,
            "most_common": common[0][0], "most_common_freq": common[0][1]
        }
    )

def clean_string(text):
    clean_text = text.lower()
    clean_text = re.sub('[^0-9a-zA-Z //]+', '', clean_text)
    return clean_text.strip()

#create document properties
corpus = CategorizedPlaintextCorpusReader(
    'C:/Users/gavin_000/Python/texts',
    r'.*\.txt',
    cat_pattern=r'(\w+)/*'
)

stop = stopwords.words('english')

results = pd.DataFrame()

for category in corpus.categories():
    for document in corpus.fileids(category):
        doc_properties = create_document_properties(category, document)
        results = results.append(doc_properties, ignore_index=True)

print results
