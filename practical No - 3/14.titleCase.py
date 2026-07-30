sentence = input("Enter the sentence: ")

result = ""
newWord = True

for ch in sentence:

    if newWord == True and 'a' <= ch <= 'z':
        ch = chr(ord(ch) - 32)

    result = result + ch

    if ch == " ":
        newWord = True
    else:
        newWord = False

print("Title Case:", result)