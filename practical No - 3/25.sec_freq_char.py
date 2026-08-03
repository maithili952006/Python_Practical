string = input("Enter the string: ")

first_char = ""
second_char = ""

first_count = 0
second_count = 0

for ch in string:

    count = 0

    for i in string:
        if ch == i:
            count += 1

    if count > first_count:
        second_count = first_count
        second_char = first_char

        first_count = count
        first_char = ch

    elif count > second_count and ch != first_char:
        second_count = count
        second_char = ch

print("Second most frequent character:", second_char)
print("Frequency:", second_count)