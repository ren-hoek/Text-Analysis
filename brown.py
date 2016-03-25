from nltk.corpus import brown
from nltk import bigrams
from nltk import FreqDist
from nltk.corpus import stopwords
from collections import Counter
import json
import re

def clean_string(text):
    clean_text = text.lower()
    clean_text = re.sub('[^0-9a-zA-Z //]+', '', clean_text)
    return clean_text.strip()

stop = stopwords.words('english')

news_word = (
        [x for x in
            [clean_string(x) for x in brown.words(categories=['news'])]
        if x and x not in stop]
        )

news_sent = []
for sent in brown.sents(categories=['news']):
    words = []
    for w in sent:
        wd = clean_string(w)
        if wd != "" and wd not in stop:
            words.append(wd)
    news_sent.append(words)

vertex = []
for sentence in news_sent:
    for bigram in bigrams(sentence):
        vertex.append(bigram)

vertices = zip(Counter(vertex).keys(), Counter(vertex).values())

word_freq = FreqDist(news_word)
freq = word_freq.most_common(20)
common = [x[0] for x in freq]

nodes = [{"id":i, "word":x[0], "freq":x[1]} for i, x in enumerate(freq)]

links=[]
for v in vertices:
    if v[0][0] in common and v[0][1] in common:
        for x in nodes:
            if x['word']==v[0][0]:
                source=x['id']
            elif x['word']==v[0][1]:
                target=x['id']
        links.append({"source":source, "target":target, "value":v[1]})

graph = {"nodes": nodes, "links":links}

with open('graph.json', 'w') as json_file:
    json.dump(graph, json_file)
