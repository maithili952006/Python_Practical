import re

phone = input("Enter your phone number: ")

pattern = r"^[6-9][0-9]{9}$"

if re.match(pattern, phone):
    print("Phone number is valid")
else:
    print("Phone number is invalid")