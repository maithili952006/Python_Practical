string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if len(string1) == len(string2):
    print("Move forward")
else:
    print("Stop the program")

string1 = string1.lower()
string2 = string2.lower()

string1 = string1.replace(" ", "")
string2 = string2.replace(" ", "")

dict1 = {}
dict2 = {}

for ch in string1:
    if ch.isalpha():
        if ch in dict1:
            dict1[ch] += 1
        else:
            dict1[ch] = 1

for ch in string2:
    if ch.isalpha():
        if ch in dict2:
            dict2[ch] += 1
        else:
            dict2[ch] = 1

if dict1 == dict2:
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")