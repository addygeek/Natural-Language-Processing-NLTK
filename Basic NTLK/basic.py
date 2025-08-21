import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = "Natural Language Processing with NLTK is fun!"


tokens = word_tokenize(text)

print("Tokens:", tokens)