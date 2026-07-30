word = input("Enter the word : ")
vowels = 0
consonants = 0
spaces = 0
digit = 0
special = 0

for ch in word:
    if('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        
        if(ch =='A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' or ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            vowels += 1
        else:
            consonants += 1
            
    elif(ch == ' '):
        spaces += 1
        
    elif('0' <= ch <= '9'):
        digit += 1
        
    else:
        special += 1
print("Vowels : ", vowels)
print("Consonants :", consonants)
print("Digits : ", digit)
print("Special character : ", special)
print("Spaces : ", spaces)                    