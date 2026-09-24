def greet(name, message="Welcome"):
    print(message, name)
    
def add(a,b):
    print("Addition = ", a + b)
    
def student(name, age):
    print("Name : ",name)
    print("Age : ",age)    
    
def total(*numbers):
    print("Numbers:", numbers)
    print("Total : ", sum(numbers)) 
    
def display_details(**details):
    print("Student Details : ")       
    
    for key, value in details.items():
        print(key,":",value)
        
greet("Rahul")       
greet("Rahul","Good Morning")
add(10,20)
student(name="Rahul",age=20)
total(10,20,30,40) 
    
    