import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
nltk.download('wordnet', quiet=True)
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
print(lemmatizer.lemmatize("running", pos='v'))
print(stemmer.stem("running"))