n = int(input("enter the number : "))
i = 2

while i < n:
    if n % i == 0:
        print("Not a prime number")
        break;
    i+=1
else:
    if n > 1:
        print("Prime number")
    else:
        print("Number is not prime")
            
