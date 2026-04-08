# Lists - Operations, Methods, and Functions

# Creating a List

numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# Accessing Elements

print("\nFirst element:", numbers[0])
print("Last element:", numbers[-1])

# List Slicing

print("\nFirst 3 elements:", numbers[:3])
print("From index 2:", numbers[2:])

# List Operations

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5]
print("\nConcatenation:", list1 + list2)

# Repetition
print("Repetition:", list1 * 2)

# Membership
print("Is 20 in numbers?", 20 in numbers)

# List Methods

nums = [1, 2, 3]

# Add element
nums.append(4)
print("\nAfter append:", nums)

# Insert element
nums.insert(1, 10)
print("After insert:", nums)

# Remove element
nums.remove(3)
print("After remove:", nums)

# Pop element
nums.pop()
print("After pop:", nums)

# Sort list
nums.sort()
print("After sort:", nums)

# Reverse list
nums.reverse()
print("After reverse:", nums)

# Built-in Functions

values = [5, 2, 8, 1]

print("\nLength:", len(values))
print("Maximum:", max(values))
print("Minimum:", min(values))
print("Sum:", sum(values))