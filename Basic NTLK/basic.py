import nltk
from nltk.tokenize import word_tokenize

nltk.data.path.append(r"C:\Users\adity\AppData\Roaming\nltk_data")

nltk.download('punkt_tab', quiet=True)

text = "Natural Language Processing with NLTK is fun!"

tokens = word_tokenize(text)

print("Tokens:", tokens)
