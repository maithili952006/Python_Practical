import re

email = input("Enter Email: ")

pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}"

if re.fullmatch(pattern, email):
    print("True")
else:
    print("False")
    
    
    
    
    
   