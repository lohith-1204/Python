# Conditional Statements in Python

# Simple if statement

age = 18

if age >= 18:
    print("You are eligible to vote")

# if-else statement

num = 10

if num % 2 == 0:
    print("\nEven number")
else:
    print("\nOdd number")

# if-elif-else statement

marks = 75

if marks >= 90:
    print("\nGrade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# Nested if

number = 5

if number > 0:
    if number % 2 == 0:
        print("\nPositive Even Number")
    else:
        print("\nPositive Odd Number")
else:
    print("\nNegative Number or Zero")

# Using input (optional)

value = int(input("\nEnter a number: "))

if value > 0:
    print("Positive")
elif value < 0:
    print("Negative")
else:
    print("Zero")