from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Child class
class Dog(Animal):

    def sound(self):
        print("Dog barks")

# Create object
obj = Dog()
obj.sound()