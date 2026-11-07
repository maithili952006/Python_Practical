# Create a set
a = {10, 20, 30, 40, 50}

print("Original Set:", a)

# 1. add()
a.add(60)
print("After add:", a)

# 2. update()
a.update([70, 80])
print("After update:", a)

# 3. remove()
a.remove(30)
print("After remove:", a)

# 4. discard()
a.discard(40)
print("After discard:", a)

# 5. pop()
a.pop()
print("After pop:", a)

# 6. copy()
b = a.copy()
print("Copied Set:", b)

# 7. union()
x = {1, 2, 3}
y = {3, 4, 5}
print("Union:", x.union(y))

# 8. intersection()
print("Intersection:", x.intersection(y))

# 9. difference()
print("Difference:", x.difference(y))

# 10. clear()
b.clear()
print("After clear:", b)