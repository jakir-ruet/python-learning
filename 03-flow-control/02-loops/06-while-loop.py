# Basic while loop
counter = 0
while counter <= 3:
    print("Counter is:", counter)
    counter += 1  # Increment counter

# Infinite while loop
while True:
    print("This will print forever")

# Break statement while loop
counter = 0
while counter < 5:
    if counter == 3:
        break  # Exit loop when counter reaches 3
    print("Counter is:", counter)
    counter += 1

# Continue statement while loop
counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        continue  # Skip the rest of the loop when counter is 3
    print("Counter is:", counter)

# User input with a while loop
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter a command (type 'quit' to exit): ")
    print(f"You entered: {user_input}")