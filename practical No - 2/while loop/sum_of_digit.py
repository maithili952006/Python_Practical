n = int(input("Enter the number : "))

sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print("Sum of the digit = ", sum)    