import nltk
from nltk.stem import PorterStemmer

# Create an object
ps = PorterStemmer()

# List of words
words = ["playing", "played", "plays", "running", "runner"]

# Apply stemming
for word in words:
    print(word, ":", ps.stem(word))