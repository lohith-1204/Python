# While Loop, Break, Continue, Nested Loops

# While Loop

print("While Loop Example:")
i = 1

while i <= 5:
    print(i)
    i += 1

# Break Statement

print("\nBreak Example:")
i = 1

while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

# Continue Statement

print("\nContinue Example:")
i = 1

while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# Nested Loops

print("\nNested Loop Example:")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)