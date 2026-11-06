string = input("Enter the string : ")

rev = ""

for ch in string:
    rev = ch + rev

if rev == string:
    print("Palindrome")
else:
    print("Not palindrome")        
    