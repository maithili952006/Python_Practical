import os

dir_name = "test_folder"

if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created.")

print("Is directory?:", os.path.isdir(dir_name))

print("Current Directory Contents:", os.listdir("."))

os.rmdir(dir_name)
print(f"Directory '{dir_name}' removed.")