import re

password = input("Enter your password: ")

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&*!]).{8,}$"

if re.match(pattern, password):
    print("Password is valid")
else:
    print("Password is invalid")