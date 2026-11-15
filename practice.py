class Animal:
    
    def sound(self):
        print("The animal has the sound")
        
class Dog(Animal):
    
    def sound(self):
        print("Dog bark")
        
obj = Dog()
obj.sound()        