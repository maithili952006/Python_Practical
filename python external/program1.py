file = open("sample.txt","w")

file.write("Hello World\n")
file.write("Welcome to python progragramming.\n")
file.write("This is a file in the python")

file.close()

file=open("sample.txt","r")

content = file.read()

print("Content of the file : ")
print(content)

file.close()