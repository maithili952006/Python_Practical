students = []
grades = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    grade = int(input("Enter grade: "))
    students.append(name)
    grades.append(grade)

print("\nStudent Details")
for i in range(len(students)):
    print(students[i], "-", grades[i])

name = input("\nEnter student name to update: ")

if name in students:
    index = students.index(name)
    new_grade = int(input("Enter new grade: "))
    grades[index] = new_grade
else:
    print("Student not found")

name = input("\nEnter student name to remove: ")

if name in students:
    index = students.index(name)
    students.pop(index)
    grades.pop(index)
else:
    print("Student not found")

print("\nFinal Student List")
for i in range(len(students)):
    print(students[i], "-", grades[i])

average = sum(grades) / len(grades)
print("\nAverage Grade =", average)

print("Highest Grade =", max(grades))
print("Lowest Grade =", min(grades))