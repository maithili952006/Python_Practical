text = input("Enter the paragraph: ")

words = text.split()

print("Total Words =", len(words))

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:")
for word in frequency:
    print(word, ":", frequency[word])

print("Top 3 Frequent Words:")

count = 0
for word in frequency:
    print(word, ":", frequency[word])
    count += 1
    if count == 3:
        break

vowels = 0

for ch in text:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
        vowels += 1

print("Total Vowels =", vowels)