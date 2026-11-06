class Father:
    def show(self):
        print("This is the father class")
 
class Son(Father):
    def display(self):
        print("This is the sons class")
        
obj = Son()
obj.show()    
obj.display()            