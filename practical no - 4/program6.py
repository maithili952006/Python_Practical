book1 = input("Enter words of Book 1: ").split()
book2 = input("Enter words of Book 2: ").split()

set1 = set(book1)
set2 = set(book2)

print("Unique words in Book 1:", set1)
print("Unique words in Book 2:", set2)

print("Common words:", set1.intersection(set2))

print("Words only in Book 1:", set1.difference(set2))

print("Words only in Book 2:", set2.difference(set1))

print("Total unique words:", set1.union(set2))
print("Count of unique words:", len(set1.union(set2)))