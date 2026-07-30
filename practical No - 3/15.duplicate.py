string = input("Enter the string: ")

result = ""

for ch in string:

    count = 0

    for i in result:
        if ch == i:
            count = count + 1

    if count == 0:
        result = result + ch

print("String after removing duplicates:", result)