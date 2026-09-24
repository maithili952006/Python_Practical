from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        """Abstract method: Must be implemented by child classes"""
        pass

    def description(self):
        return "This is a vehicle."

class Car(Vehicle):
    
    def start_engine(self):
        return "Car engine started"

class Motorcycle(Vehicle):
    
    def start_engine(self):
        return "Motorcycle engine started: Broom!"

my_car = Car()
print(my_car.description())       
print(my_car.start_engine())     

my_bike = Motorcycle()
print(my_bike.description())      
print(my_bike.start_engine())     