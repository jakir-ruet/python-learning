myList = ["Mango", "Banana", "Pineapple", "Orange", "Strawberry", "Computer", "Smartphone"]

for x in range(len(myList)):  
    if x == 4:  # Stop the loop when x reaches 4
        break
    print(f"hello {x}")  # Print the index number

for y in range(9):
    if y == 4:
        break
    print(f"hello list, {y}")

for z in range(len(myList)):
    if z == 3:
        continue
    print(f"continue {z}")