file = open("data.txt", "w")

file.write("Hello Python\n")
file.write("Welcome to file handling\n")

lines = ["Hi\n", "python\n", "programming\n"]
file.writelines(lines)

file.close()

file = open("data.txt", "r")
print("File read : ")
print(file.read())
file.close()


file = open("data.txt", "r")
print(file.readline())
file.close()

file = open("data.txt", "r")
print("Using readlines():")
print(file.readlines())

file.close()

file = open("data.txt","r+")
print("Using r+, read and write the content : ")
print(file.read())
file.close()


file = open("data.txt", "r")
print(file.read(5))
print(file.tell())
file.close()


file = open("data.txt", "r")
file.seek(6)
print(file.read())
file.close()