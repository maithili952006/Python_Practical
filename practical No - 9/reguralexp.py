import re

text = """
Hello students,

For any queries, contact:
abc@gmail.com
support@yahoo.com
student123@college.edu
admin@school.org

Thank you.
"""

pattern = r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)

print("Email addresses found:")

for email in emails:
    print(email)
    
    
    
#     | Part           | Meaning                                     |
# | -------------- | ------------------------------------------- |
# | `r`            | Tells Python this is a raw string           |
# | `[\w.-]`       | Allows letters, numbers, `_`, `.`, and `-`  |
# | `+`            | One or more characters                      |
# | `@`            | Matches the `@` symbol                      |
# | `[\w.-]+`      | Matches the email domain name               |
# | `\.`           | Matches a real `.`                          |
# | `[a-zA-Z]{2,}` | Matches the ending like `com`, `org`, `edu` |
