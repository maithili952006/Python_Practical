# Create user-defined exception
#28. Write a program for creating user-defined exception
class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("Age must be 18 or above")
    else:
        print("You are eligible")

except AgeError as e:
    print("Error:", e)