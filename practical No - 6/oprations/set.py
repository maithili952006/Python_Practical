s = {10, 20, 30, 40}

print("Set:", s)

# 1. add()
s.add(50)
print("After add:", s)

# 2. remove()
s.remove(20)
print("After remove:", s)

# 3. discard()
s.discard(100)
print("After discard:", s)

# 4. pop()
x = s.pop()
print("Removed element:", x)
print("After pop:", s)

# Add elements again
s.add(20)
s.add(30)

# 5. union()
s2 = {30, 40, 50, 60}
print("Union:", s.union(s2))

# 6. intersection()
print("Intersection:", s.intersection(s2))

# 7. difference()
print("Difference:", s.difference(s2))

# 8. symmetric_difference()
print("Symmetric Difference:", s.symmetric_difference(s2))

# 9. issubset()
a = {30, 40}
print("Is subset:", a.issubset(s))

# 10. issuperset()
print("Is superset:", s.issuperset(a))