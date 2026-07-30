sentence = input("Enter the sentence: ")

word = ""
smallest = ""

count = 0
min_count = -1

for ch in sentence:

    if ch != " ":
        word = word + ch
        count = count + 1
    else:
        if min_count == -1 or count < min_count:
            min_count = count
            smallest = word

        word = ""
        count = 0

print("Smallest word =", smallest)