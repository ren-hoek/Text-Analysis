from nltk.corpus import gutenberg

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)
    
for file in gutenberg.fileids():
    path = "texts/" + file
    book = strip_non_ascii(gutenberg.raw(fileids=[file]))
    with open (path, 'w') as text_file:
        text_file.write(book)
