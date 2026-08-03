string = input("Enter the duplicate string : ")

result = ""

for ch in string:

    count = 0

    for i in result:
        if ch == i:
            count += 1

    if count == 0:
        result = result + ch

print("String after the removal of duplicate : ", result)

