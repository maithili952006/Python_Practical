string = input("Enter the string : ")
ch = input("Enter the char to search how many time occur : ")

count = 0

for i in string:
    if i == ch:
        count+= 1
print("The character",ch," occure",count)


word = "maithili"
count = {}

for ch in word:
    if ch in count:
        count[ch] = count[ch] + 1
    else:
        count[ch] = 1
 
for ch in count:
    print(ch,"=",count[ch])            
    
    
word = input("Enter a word: ")

for i in range(len(word)):
    count = 0

    for j in range(len(word)):
        if word[i] == word[j]:
            count = count + 1

    if word.index(word[i]) == i:
        print(word[i], "=", count)    