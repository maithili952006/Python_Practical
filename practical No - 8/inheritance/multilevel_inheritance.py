class Grandfather:
    def property(self):
        print("Grandfather has property")
        
class Father(Grandfather):
    def car(self):
        print("Father has a car")
        
class Son(Father):
    def bike(self):
        print("Son has a bike")
        
s = Son()
s.property()
s.car()
s.bike()            
            