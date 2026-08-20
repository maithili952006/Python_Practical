# Tuple

t = (10, 20, 30, 20, 40)

print("Tuple:", t)

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

# 7. Concatenation
t2 = (50, 60)
print("Concatenation:", t + t2)

# 8. Repetition
print("Repetition:", t2 * 2)

# 9. Slicing
print("Slicing:", t[1:4])

# 10. Membership
print("Is 30 present?", 30 in t)