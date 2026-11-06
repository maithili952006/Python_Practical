string = input("Enter the string : ")
upper = 0
lower = 0
countU = 0
countL = 0

for ch in string:
    if('A' <= ch <= 'Z'):
        countU += 1
    elif('a' <= ch <= 'z'):
        countL += 1    
    else:
        print("None")    
        
print("The uppercase letter count is : ",countU)
print("The lower case letter count is : ",countL)        