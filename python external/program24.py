import nltk
from nltk.tokenize import word_tokenize

# Input sentence
text = "Python is a popular programming language."

# Apply tokenization
tokens = word_tokenize(text)

# Display tokens
print("Original Sentence:", text)
print("Tokens:", tokens)