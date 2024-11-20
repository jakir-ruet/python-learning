# Looping through a list
fruits = ["Apple", "Mango", "Banana"]
for fruit in fruits:
    print(fruit)

# Looping through a string
word = "Bangladesh"
for letter in word:
    print(letter)

# Using range() with a for loop
# The range() function is commonly used in for loops to generate a sequence of numbers.
for i in range(5):  # This will iterate over the numbers 0 to 4
    print(i)

for i in range(1, 10, 3):  # Start at 1, stop before 10, step by 2
    print(i)

# Nested for loop
for i in range(3):       # Outer loop
    for j in range(3):   # Inner loop
        print(f"i = {i}, j = {j}")

# Iterating over a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"{key}: {value}")
