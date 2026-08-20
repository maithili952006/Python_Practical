import os

file = open("demo.txt", "w")
file.write("Hello Python\n")
file.write("This is a file operation program.")
file.close()

print("File created and data written.")

file = open("demo.txt", "r")
data = file.read()
file.close()

print("\nFile content:")
print(data)

file = open("demo.txt", "a")
file.write("\nNew line added.")
file.close()

print("\nData appended successfully.")

file = open("demo.txt", "r")
print("\nUpdated file:")
print(file.read())
file.close()

os.rename("demo.txt", "newdemo.txt")
print("\nFile renamed successfully.")

if os.path.exists("newdemo.txt"):
    print("File exists.")

os.remove("newdemo.txt")
print("File deleted successfully.")