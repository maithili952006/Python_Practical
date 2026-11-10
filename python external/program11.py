#mutlilevel inheritance
class Grandfather:
    def show(self):
        print("This is the grandfather class")
        
class Father(Grandfather):
    def display(self):
        print("This is the fahter class")
        
class Son(Father):
    def print_data(Father):
        print("THis is the son's class")       
        
obj = Son()
obj.show()
obj.display()
obj.print_data()          