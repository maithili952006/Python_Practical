string = input("Enter the string: ")

result = ""
count = 1

for i in range(len(string) - 1):

    if string[i] == string[i + 1]:
        count += 1
    else:
        result = result + string[i] + str(count)
        count = 1

result = result + string[len(string) - 1] + str(count)

if len(result) < len(string):
    print("Compressed String:", result)
else:
    print("Original String:", string)