string = input("Enter the string : ")
sub = input("Enter the substring to search : ")

found = 0

for i in range(len(string) - len(sub) + 1):
    
    if string[i:i + len(sub)] == sub:
        found = 1
        break
    
if found == 1:
    print("Substring found")
else:
    print("Substring not found")    