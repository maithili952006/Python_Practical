class Father:
    def house(self):
        print("Father has a house")
      
class Mother:
    def car(self):
        print("Mother has a car")        
        
class Child(Father, Mother):
    def bike(self):
        print("Child has a bike")        
   
c = Child()
c.house()
c.car()
c.bike()        