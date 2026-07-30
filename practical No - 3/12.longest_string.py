sentence = input("Enter the sentence : ")

word = ""
longest = ""

count = 0
max = 0

for ch in sentence:
    if ch != " ":
        word = word + ch
        count = count + 1
    else:
        if count > max:
            max = count
            longest = word
        word = ""
        count = 0
print("The longest word is : ",longest)        
        
