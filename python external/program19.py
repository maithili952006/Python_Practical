# Create a tuple
t = (10, 20, 30, 40, 50, 20)

print("Original Tuple:", t)

# 1. count()
print("Count of 20:", t.count(20))

# 2. index()
print("Index of 30:", t.index(30))

# 3. len()
print("Length:", len(t))

# 4. max()
print("Maximum:", max(t))

# 5. min()
print("Minimum:", min(t))

# 6. sum()
print("Sum:", sum(t))

# 7. sorted()
print("Sorted Tuple:", sorted(t))

# 8. tuple()
a = tuple([1, 2, 3])
print("Converted Tuple:", a)

# 9. Concatenation
b = t + a
print("After Concatenation:", b)

# 10. Repetition
c = a * 2
print("After Repetition:", c)