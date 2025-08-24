import nltk
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)
tokens = nltk.word_tokenize("Apple is opening a new office in New York.")
print(nltk.ne_chunk(nltk.pos_tag(tokens)))