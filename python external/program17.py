# Create a dictionary
student = {
    "name": "Rahul",
    "roll": 101,
    "marks": 85
}

print("Original Dictionary:", student)

# 1. keys()
print("Keys:", student.keys())

# 2. values()
print("Values:", student.values())

# 3. items()
print("Items:", student.items())

# 4. get()
print("Name:", student.get("name"))

# 5. update()
student.update({"marks": 90})
print("After update:", student)

# 6. pop()
student.pop("roll")
print("After pop:", student)

# 7. copy()
b = student.copy()
print("Copied Dictionary:", b)

# 8. setdefault()
student.setdefault("city", "Kolhapur")
print("After setdefault:", student)

# 9. popitem()
student.popitem()   #Removes the last inserted key-value pair.
print("After popitem:", student)

# 10. clear()
b.clear()
print("After clear:", b)