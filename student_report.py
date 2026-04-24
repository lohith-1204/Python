# Day 24: Student Report Card System (OOP)

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # encapsulation

    # Calculate total
    def total(self):
        return sum(self.__marks.values())

    # Calculate average
    def average(self):
        return self.total() / len(self.__marks)

    # Calculate grade (abstraction)
    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

    # Display report
    def display(self):
        print("\n===== Report Card =====")
        print("Name:", self.name)

        print("\nMarks:")
        for subject, mark in self.__marks.items():
            print(subject, ":", mark)

        print("\nTotal:", self.total())
        print("Average:", self.average())
        print("Grade:", self.grade())


# -------------------------------
# Main Program
# -------------------------------

name = input("Enter student name: ")

subjects = ["Math", "Science", "English"]
marks = {}

for sub in subjects:
    marks[sub] = int(input(f"Enter marks for {sub}: "))

student = Student(name, marks)
student.display()