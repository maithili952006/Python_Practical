string = input("Enter the string: ")

max_count = 0
max_char = ""

for ch in string:

    count = 0

    for i in string:
        if ch == i:
            count += 1

    if count > max_count:
        max_count = count
        max_char = ch

print("Most frequent character:", max_char)
print("Frequency:", max_count)