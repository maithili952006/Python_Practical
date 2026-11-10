file = open("sample.txt","w")
file.write("Hello i am maithili")
file.close()

file1 = open("sample.txt")
data = file1.read()
file1.close()

file1= open("sample.txt")
print(data)
file1.close()