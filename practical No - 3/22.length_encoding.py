string = input("Enter the string : ")

count = 1

for i in range(len(string) - 1):
    
    if string[i] == string[i+1]:
        count += 1
    else:
        print(string[i] + str(count),end="")    
        count = 1
print(string[len(string) - 1] + str(count))