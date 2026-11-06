class Father:
    def show(self):
        print("This is Father class")

class Mother:
    def display(self):
        print("This is the mother class")
  
class Child(Father,Mother):
    def print_data(self):
        print("This is the child class")
        
obj = Child()                
obj.show()
obj.display()
obj.print_data()