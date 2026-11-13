#27. Write a program for demonstrating 
# abstract class and methods using python
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