#Tuples and Sets in Python

# Tuples

# Creating a tuple
my_tuple = (10, 20, 30, 40)

print("Tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing
print("Sliced tuple:", my_tuple[1:3])

# Tuple operations
t1 = (1, 2)
t2 = (3, 4)

print("\nTuple Concatenation:", t1 + t2)
print("Tuple Repetition:", t1 * 2)

# Sets

# Creating a set
my_set = {1, 2, 3, 4, 4}
print("\nSet (duplicates removed):", my_set)

# Adding elements
my_set.add(5)
print("After add:", my_set)

# Removing elements
my_set.remove(2)
print("After remove:", my_set)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("\nUnion:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)