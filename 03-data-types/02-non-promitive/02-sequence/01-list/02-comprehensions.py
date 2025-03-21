numbers = [2, 1, 4, 6, 7, 8, 9]
square = []
for number in numbers:
   square.append(number**2)
print(square)

# OR
square = [number**2 for number in numbers]
print(square)