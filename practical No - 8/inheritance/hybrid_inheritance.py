class Animal:
    def eat(self):
        print("Animal eats")
 
class Dog(Animal):
    def bark(self):
        print("Dog barks")
      
class Cat(Animal):
    def meow(self):
        print("Cat meows")

class Hybrid(Dog, Cat):
    def play(self):
        print("Hybrid plays")
       
h = Hybrid()

h.eat()                         
h.bark()
h.meow()
h.play()
        