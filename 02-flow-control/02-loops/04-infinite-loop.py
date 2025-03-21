# Infinite while loop
while True:
    print("This will print forever")

count = 0
while True:
    count += 1
    print(f"Loop iteration {count}")
    if count == 5:
        print("Exiting loop...")
        break  # Exit the loop when count reaches 5
