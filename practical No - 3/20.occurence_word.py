sentence = input("Enter the string : ")
word = input("Enter the word to serach : ")

count = 0
words = sentence.split()

for i in words:
    if i == word:
        count += 1
            
print("Occurences = ",count)