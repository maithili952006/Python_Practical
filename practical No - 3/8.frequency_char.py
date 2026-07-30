string = input("Enter the string : ")
ch = input("Enter the char to search how many time occur : ")

count = 0

for i in string:
    if i == ch:
        count+= 1
print("The character",ch," occure",count)
