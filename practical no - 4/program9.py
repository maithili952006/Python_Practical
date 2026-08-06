attendance = {
    "Monday": {"Rahul", "Amit", "Priya"},
    "Tuesday": {"Rahul", "Priya"},
    "Wednesday": {"Rahul", "Amit"},
    "Thursday": {"Rahul", "Priya"},
    "Friday": {"Rahul", "Neha"}
}

# Students who attended all classes
all_students = attendance["Monday"]

for day in attendance:
    all_students = all_students.intersection(attendance[day])

print("Students who attended all classes:", all_students)

# Students who attended at least one class
unique_students = set()

for day in attendance:
    unique_students = unique_students.union(attendance[day])

print("Total Unique Students:", len(unique_students))

# Students who attended only one class
student_count = {}

for day in attendance:
    for student in attendance[day]:
        if student in student_count:
            student_count[student] += 1
        else:
            student_count[student] = 1

print("Students who attended only one class:")

for student in student_count:
    if student_count[student] == 1:
        print(student)