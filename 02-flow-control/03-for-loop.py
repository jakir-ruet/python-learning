myList = ["Mango", "Banana", "Apple", True, 50]
for i in myList:
    print("The list using loop", i)

# using break statement
for b in myList:
    if b == "Banana":
        break
    print("using break", b)

# using continue statement
for c in myList:
    if c == "Banana":
        continue
    print("using continue", c)

# using range function
# iterate over the list index
for i in range(len(myList)):
    print("using range", myList[i])
