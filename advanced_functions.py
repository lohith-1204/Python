# Lambda, Recursion, *args and **kwargs

# Lambda Functions

# Normal function
def square(x):
    return x * x

print("Square using normal function:", square(5))

# Lambda function
square_lambda = lambda x: x * x
print("Square using lambda:", square_lambda(5))

# Lambda with multiple arguments
add = lambda a, b: a + b
print("Addition using lambda:", add(3, 4))

# Recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))

# *args (Multiple Arguments)

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print("\nSum using *args:", sum_all(1, 2, 3, 4))

# **kwargs (Keyword Arguments)

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print("\nDetails using **kwargs:")
print_details(name="Lohith", age=21, course="ISE")