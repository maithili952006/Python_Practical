n = int(input("Enter the num : "))
i = 1

num = int(input("Enter the values : "))
smallest = num

while i < n:
    num = int(input("Enter the number : "))
    if num < smallest:
        smallest = num
    i+=1
print("Smallest number is : ",smallest)        