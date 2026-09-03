import nltk
from nltk.tokenize import sent_tokenize

text = "Python is easy to learn. It is a popular language."

sentences = sent_tokenize(text)

print(sentences)