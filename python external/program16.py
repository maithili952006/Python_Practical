# Create a list
a = [10, 20, 30, 40, 50]

print("Original List:", a)

# 1. append()
a.append(60)
print("After append:", a)

# 2. insert()
a.insert(1, 15)
print("After insert:", a)

# 3. remove()
a.remove(30)
print("After remove:", a)

# 4. pop()
a.pop()
print("After pop:", a)

# 5. index()
print("Index of 40:", a.index(40))

# 6. count()
print("Count of 20:", a.count(20))

# 7. sort()
a.sort()
print("After sort:", a)

# 8. reverse()
a.reverse()
print("After reverse:", a)

# 9. copy()
b = a.copy()
print("Copied List:", b)

# 10. clear()
b.clear()
print("After clear:", b)