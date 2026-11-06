class Father:
    def show(self):
        print("This is Father class")
    
class Son(Father):
    def display(self):
        print("This is son class")        
        
class Daughter(Father):
    def print_data(self):
        print("This is the daughter class")

obj1 = Son()
obj2 = Daughter()

obj1.show()
obj1.display()

obj2.show()
obj2.print_data()               