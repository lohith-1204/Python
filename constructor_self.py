# Constructor, self keyword, Optional Parameters

# Constructor (__init__)

class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Create object
s1 = Student("Lohith", 21)
s1.display()

# self Keyword

class Example:

    def show(self):
        print("\nThis is self keyword example")


e1 = Example()
e1.show()

# self refers to the current object

# Optional (Default) Parameters

class Person:

    def __init__(self, name, age=18):   # default value for age
        self.name = name
        self.age = age

    def display(self):
        print("\nName:", self.name)
        print("Age:", self.age)


# Object with both parameters
p1 = Person("Rahul", 22)
p1.display()

# Object with default parameter
p2 = Person("Anita")
p2.display()