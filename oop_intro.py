# Object-Oriented Programming (OOP) - Introduction

# Define a Class

class Student:
    
    # Constructor (called automatically)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method (function inside class)
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Create Object

student1 = Student("Lohith", 21)

# Access attributes
print("Student Name:", student1.name)

# Call method
student1.display()

# Another Object

student2 = Student("Rahul", 22)
student2.display()