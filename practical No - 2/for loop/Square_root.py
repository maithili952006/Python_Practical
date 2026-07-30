n = int(input("Enter number: "))

root = 0

# Find square root manually
for i in range(1, n + 1):
    if i * i == n:
        root = i
        break

if root == 0:
    print("The number is not a perfect square.")
else:
    print("Square root =", root)

    prime = True

    if root < 2:
        prime = False
    else:
        for i in range(2, root):
            if root % i == 0:
                prime = False
                break

    if prime:
        print("Prime")
    else:
        print("Not Prime")