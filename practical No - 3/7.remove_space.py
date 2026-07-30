string = input("Enter the string : ")

result = ""
for ch in string:
    if ch != " ":
        result = result + ch
print("The string is : ",result)
        