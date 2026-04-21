# Advanced OOP Concepts

# Getters and Setters

class Student:
    
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Invalid marks")


s1 = Student("Lohith", 80)

print("Marks:", s1.get_marks())

s1.set_marks(90)
print("Updated Marks:", s1.get_marks())


# Method Overloading 


class Calculator:

    def add(self, a, b=0, c=0):   # default arguments
        return a + b + c


calc = Calculator()

print("\nAdd 2 numbers:", calc.add(5, 3))
print("Add 3 numbers:", calc.add(5, 3, 2))


# Method Overriding

class Animal:
    
    def sound(self):
        print("\nAnimal makes sound")


class Dog(Animal):
    
    def sound(self):   # overriding
        print("Dog barks")


d = Dog()
d.sound()


# Abstract Class

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rect = Rectangle(5, 4)
print("\nArea of rectangle:", rect.area())