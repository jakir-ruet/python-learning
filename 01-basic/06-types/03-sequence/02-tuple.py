myTuple = ["Mango", "Banana", "Apple", "Mango", True, 45]
print(myTuple)
print(len(myTuple))
print(myTuple[0])
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# mySingleTuple = ("Mango") #this is not tuple it is work as string
# print(mySingleTuple)
# print(type(mySingleTuple))
mySingleTuple = ("Mango",)  # this is tuple
print(mySingleTuple)
print(type(mySingleTuple))

#tuple constructor
myConstTuple = tuple(("Mango", "Banana", "Apple"))
print("This tuple constructor", myConstTuple)