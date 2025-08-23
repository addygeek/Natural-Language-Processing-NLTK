import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize, TweetTokenizer



# Download required resources
nltk.download('punkt')

text = "Hello there! How's everything going? NLP is fun. #AI #NLP"

# 1. Word Tokenization
words = word_tokenize(text)
print("Word Tokenization:", words)

# 2. Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentence Tokenization:", sentences)

# 3. Regular Expression Tokenization
pattern = r'\w+'
regexp_tokens = regexp_tokenize(text, pattern)
print("Regexp Tokenization:", regexp_tokens)

# 4. Tweet Tokenization (handles hashtags, emojis, etc.)
tweet_tokenizer = TweetTokenizer()
tweet_tokens = tweet_tokenizer.tokenize(text)
print("Tweet Tokenization:", tweet_tokens)