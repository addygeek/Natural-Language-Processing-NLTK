import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize, TweetTokenizer, MWETokenizer
from nltk.corpus import stopwords
import re

# Download required NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

text = """
Dr. Smith, who works at the U.N., said: "Natural Language Processing (NLP) is fascinating! 
Visit https://www.nltk.org/ for more info. #NLP #AI"
Email me at example@example.com.
"""

# 1. Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentence Tokenization:")
for i, sent in enumerate(sentences, 1):
    print(f"{i}: {sent}")

print("\n" + "-"*50 + "\n")

# 2. Word Tokenization
words = word_tokenize(text)
print("Word Tokenization:")
print(words)

print("\n" + "-"*50 + "\n")

# 3. Regular Expression Tokenization (splitting on non-word characters)
pattern = r'\w+'
regexp_tokens = regexp_tokenize(text, pattern)
print("Regexp Tokenization:")
print(regexp_tokens)

print("\n" + "-"*50 + "\n")

# 4. Tweet Tokenizer (handles hashtags, mentions, emojis, etc.)
tweet_tokenizer = TweetTokenizer()
tweet_tokens = tweet_tokenizer.tokenize(text)
print("Tweet Tokenization:")
print(tweet_tokens)

print("\n" + "-"*50 + "\n")

# 5. Multi-Word Expression Tokenizer
mwe_tokenizer = MWETokenizer([('Natural', 'Language', 'Processing'), ('New', 'York')])
mwe_tokens = mwe_tokenizer.tokenize(word_tokenize(text))
print("Multi-Word Expression Tokenization:")
print(mwe_tokens)

print("\n" + "-"*50 + "\n")

# 6. Removing Stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in word_tokenize(text) if w.lower() not in stop_words]
print("Tokens after Stopword Removal:")
print(filtered_tokens)

print("\n" + "-"*50 + "\n")

# 7. Custom Tokenization: Extracting emails and URLs

email_pattern = r'[\w\.-]+@[\w\.-]+'
url_pattern = r'https?://[^\s]+'

emails = re.findall(email_pattern, text)
urls = re.findall(url_pattern, text)

print("Extracted Emails:")
print(emails)
print("Extracted URLs:")
print(urls)