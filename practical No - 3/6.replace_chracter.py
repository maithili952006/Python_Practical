string = input("Enter the string : ")
old = input("Enter the old charater : ")
new = input("Enter the new string : ")

result  = ""
for ch in string:
    if ch == old:
        result = result + new
    else:
        result = result + ch
print("Original string = ",string)
print("New String = ",result)
    