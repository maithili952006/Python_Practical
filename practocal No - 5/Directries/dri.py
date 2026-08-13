import os

os.mkdir("MyFolder")
print("Directory created")

print("Directory exists:", os.path.exists("MyFolder"))

print("Current directory:", os.getcwd())

os.chdir("MyFolder")
print("Changed directory:", os.getcwd())


os.chdir("..")

print("Files and directories:")
print(os.listdir())

os.rename("MyFolder", "NewFolder")
print("Directory renamed")

os.rmdir("NewFolder")
print("Directory removed")










# import os

# folder = "MyFolder"

# os.mkdir(folder)

# print("Directory Created")
# print("Name:", folder)
# print("Path:", os.path.abspath(folder))

# print("\nChecking Directory")
# print("Exists:", os.path.exists(folder))
# print("Is Directory:", os.path.isdir(folder))

# print("\nCurrent Working Directory")
# print("Path:", os.getcwd())

 
# os.chdir(folder)

# print("\nChanged Directory")
# print("Current Path:", os.getcwd())

# os.chdir("..")

# print("\nReturned to Parent Directory")
# print("Current Path:", os.getcwd())


# print("\nFiles and Directories")
# print(os.listdir())

# new_folder = "NewFolder"

# os.rename(folder, new_folder)

# print("\nDirectory Renamed")
# print("Old Name:", folder)
# print("New Name:", new_folder)
# print("New Path:", os.path.abspath(new_folder))

# print("\nChecking New Directory")
# print("Exists:", os.path.exists(new_folder))
# print("Is Directory:", os.path.isdir(new_folder))

# os.rmdir(new_folder)

# print("\nDirectory Removed")
# print("Removed Directory:", new_folder)
# print("Removed Path:", os.path.abspath(new_folder))

# print("\nChecking After Removal")
# print("Exists:", os.path.exists(new_folder))