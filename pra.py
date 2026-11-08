import os

print("Cureent working directry",os.getcwd())

os.mkdir("My_dir11")

print("The all directry are : ",os.listdir())

os.chdir("My_dir")
print("Changed dir :",os.getcwd())

os.mkdir("Subfolder")
print("The sub folder")

print(os.path.exists("Subfolder"))

print(os.path.isdir("Subfolder"))

os.rename("subfolder","newfolder")

os.rmdir("Newfolder")

os.chdir("...")
print("Get back to the parent directry")