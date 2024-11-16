# Outer loop: iterating over rows
for i in range(3):
    # Inner loop: iterating over columns
    for j in range(3):
        print(f"i = {i}, j = {j}")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # Move to the next line after printing all elements in a row

for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print("Breaking the loop at i = 1, j = 1")
            break
    else:
        # Only executed if inner loop wasn't broken
        continue
    break  # This will break the outer loop as well
