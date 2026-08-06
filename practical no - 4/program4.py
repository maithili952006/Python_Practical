
project1 = {"Rahul", "Amit", "Priya", "Sneha"}

project2 = {"Priya", "Sneha", "Rohan", "Neha"}

print("Project 1:", project1)
print("Project 2:", project2)

print("Common Employees:", project1 & project2)

print("Only in Project 1:", project1 - project2)

print("Only in Project 2:", project2 - project1)

print("Total Unique Employees:", project1 | project2)