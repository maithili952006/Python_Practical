import os

# 1. Get current working directory
print("Current Directory:", os.getcwd())

# 2. Create a new directory
os.mkdir("MyFolder1")
print("Directory created successfully")

# 3. List all files and directories
print("Directory Contents:", os.listdir())

# 4. Change current working directory
os.chdir("MyFolder")
print("Changed Directory:", os.getcwd())

# 5. Create a subdirectory
os.mkdir("SubFolder")
print("Subdirectory created")

# 6. Check whether a directory exists
print("Directory Exists:", os.path.exists("SubFolder"))

# 7. Check whether the path is a directory
print("Is Directory:", os.path.isdir("SubFolder"))

# 8. Rename a directory
os.rename("SubFolder", "NewFolder")
print("Directory renamed successfully")

# 9. Remove a directory
os.rmdir("NewFolder")
print("Directory removed successfully")

# 10. Change back to the parent directory
os.chdir("..")
print("Current Directory:", os.getcwd())