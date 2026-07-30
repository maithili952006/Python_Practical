string = input("Enter the string : ")

rev = ""

for i in string:
    rev = i + rev

if rev == string:
    print("Palindrome")
else:
    print("Not palindrome")        
    