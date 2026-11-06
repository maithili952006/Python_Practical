class Student:

    def __init__(self,name, rollNo,marks):
        self.name = name
        self.rollNo = rollNo
        self.marks = marks
        
    def display(self):
        print("Student name :",self.name)
        print("Roll number : ", self.rollNo)
        print("Marks:",self.marks) 
        
        
s1 = Student("Maithili",101,99) 

s1.display()       