# Iterator Example

numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# Generator Example

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

for value in gen:
    print(value)

    # List
nums = [x**2 for x in range(5)]
print(nums)

# Generator
gen = (x**2 for x in range(5))
print(gen)

for i in gen:
    print(i)