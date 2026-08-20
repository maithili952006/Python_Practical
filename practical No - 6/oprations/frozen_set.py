s = frozenset([10, 20, 30, 40])

print("Frozen Set:", s)

# 1. len()
print("Length:", len(s))

# 2. union()
s2 = frozenset([30, 40, 50, 60])
print("Union:", s.union(s2))

# 3. intersection()
print("Intersection:", s.intersection(s2))

# 4. difference()
print("Difference:", s.difference(s2))

# 5. symmetric_difference()
print("Symmetric Difference:", s.symmetric_difference(s2))

# 6. issubset()
a = frozenset([10, 20])
print("Is subset:", a.issubset(s))

# 7. issuperset()
print("Is superset:", s.issuperset(a))

# 8. isdisjoint()
b = frozenset([100, 200])
print("Is disjoint:", s.isdisjoint(b))

# 9. Membership
print("Is 20 present?", 20 in s)

# 10. Convert to set
normal_set = set(s)
print("Converted to Set:", normal_set)