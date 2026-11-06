file = open("source.txt","w")
file.write("Hello world !\n")
file.write("Welcome to the python programming\n")
file.write("This is a file handing program")
file.close()

file1 = open("source.txt")

content = file1.read()
file1.close()

file2 = open("destination.txt","w")

file2.write(content)
file2.close()

file2 = open("destination.txt","r")
print(file2.read())
file2.close()
