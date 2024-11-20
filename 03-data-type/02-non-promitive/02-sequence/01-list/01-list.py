# its sequence type collection
# its indexed, ordered, mutable, allow dublicate
myList = ["Mango", "Banana", "Apple", "Mango", True, 45]
print(myList)
print(myList[0])
print("negative index", myList[-2])
print("Index rang", myList[2:4])
print("Exclude a item", myList[:4])
print("range of item", myList[-4:-1])
print(type(myList))
print(len(myList))
myBoolList = [True, False, True, False]
print(myBoolList)

# check the item
if "apple" in myList:
    print("yes, 'apple' is available")
else:
    print("No, 'apple not available here'")

myList[1:2] = ["Berry", "Graphs"]
print(myList)

# list constructor
myConstList = list(("Mango", "Banana", "Apple"))
print(myConstList)

myNestedList = ["Azim", "Rahim", ["Sami", "Tommy"], "Alex", ["Sony", "Jasim"], "sammy"]

print("This is my nested list", myNestedList)
print("from index 1", myNestedList[1])
print("from index 2", myNestedList[2])
print("from index 2.1", myNestedList[2][1])
