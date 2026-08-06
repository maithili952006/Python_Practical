attendance = {
    "Monday": {"Rahul", "Priya", "Amit"},
    "Tuesday": {"Rahul", "Priya"},
    "Wednesday": {"Rahul", "Amit"},
    "Thursday": {"Rahul", "Priya"},
    "Friday": {"Rahul", "Neha"}
}

all_students = attendance["Monday"]

for day in attendance:
    all_students = all_students.intersection(attendance[day])

print("Students who attended all classes:", all_students)

unique_students = set()

for day in attendance:
    unique_students = unique_students.union(attendance[day])

print("Total Unique Students:", len(unique_students))

count = {}

for day in attendance:
    for student in attendance[day]:
        if student in count:
            count[student] += 1
        else:
            count[student] = 1

print("Students who attended only one class:")

for student in count:
    if count[student] == 1:
        print(student)