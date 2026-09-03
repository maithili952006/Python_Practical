import nltk
from nltk.tokenize import word_tokenize

text = "Python is a very easy language to learn"

words = word_tokenize(text)

stopwords = ["is", "a", "very", "to"]

result = []

for word in words:
    if word not in stopwords:
        result.append(word)

print(result)