# Operators in Python

a = 10
b = 5

print("a =", a)
print("b =", b)

# Comparison Operators

print("\n--- Comparison Operators ---")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operators

print("\n--- Logical Operators ---")
x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# Assignment Operators

print("\n--- Assignment Operators ---")
num = 10

num += 5   # num = num + 5
print("After += :", num)

num -= 3   # num = num - 3
print("After -= :", num)

num *= 2   # num = num * 2
print("After *= :", num)

num /= 4   # num = num / 4
print("After /= :", num)

num %= 3   # num = num % 3
print("After %= :", num)

# Bitwise Operators

print("\n--- Bitwise Operators ---")
p = 6   # 110 in binary
q = 3   # 011 in binary

print("p & q (AND):", p & q)
print("p | q (OR):", p | q)
print("p ^ q (XOR):", p ^ q)
print("~p (NOT):", ~p)
print("p << 1 (Left Shift):", p << 1)
print("p >> 1 (Right Shift):", p >> 1)