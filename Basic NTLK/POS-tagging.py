import nltk
nltk.download('averaged_perceptron_tagger', quiet=True)
tokens = nltk.word_tokenize("NLTK is fun.")
print(nltk.pos_tag(tokens))