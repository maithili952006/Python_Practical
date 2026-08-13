with open("data.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to file handling\n")

    lines = ["hello\n", "python\n", "programming\n"]
    file.writelines(lines)

with open("data.txt", "r") as file:
    print("Using read():")
    print(file.read())


with open("data.txt", "r") as file:
    print("Using readline():")
    print(file.readline())


with open("data.txt", "r") as file:
    print("Using readlines():")
    print(file.readlines())


with open("data.txt", "r") as file:
    print("Starting position:", file.tell())
    file.read(5)
    print("After reading 5 characters:", file.tell())
    file.seek(0)
    print("After seek(0):", file.tell())