text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

data = list(frequency.items())

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i][1] < data[j][1]:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp

print("Character Frequency:")

for ch, count in data:
    print(ch, "=", count) 