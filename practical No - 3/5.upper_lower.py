string = input("Enter the string : ")
upper = 0
lower = 0
countU = 0
countL = 0

for ch in string:
    if('A' <= ch <= 'Z'):
        countU += 1
    else:
        countL += 1    
        
print("The uppercase letter count is : ",countU)
print("The lower case letter count is : ",countL)        