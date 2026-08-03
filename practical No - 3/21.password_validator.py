password = input("Enter the password : ")

upper = 0 
lower = 0
digit = 0
special = 0
length = 0

for ch in password:
    length += 1
    
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1
    elif '0' <= ch <= '9':
        digit += 1
    else:
        special += 1
        
if length >= 8 and upper >=1 and lower >=1 and digit >= 1 and special >= 1:
    print("Valid password")
else:
    print("Invalide password")                   