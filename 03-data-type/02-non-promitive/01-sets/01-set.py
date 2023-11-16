# it is a unordered, unindex collection.
# each element is unique/not dublicate and immutable.

myset = {"apple", "mango", "cherry", "banana"}
print(myset)
print(type(myset))
print("Length of set ", len(myset))

mysetUnique = {"apple", "mango", "cherry", "banana", "apple"}
print("not allow dublicate", mysetUnique)

mysetMix = {2, 3.40, "mango", 3 + 4j, True}
print(mysetMix)

# using the set() constructor to make a set
consset = ("apple", "banana", "cherry")
print(consset)

# update the set
fruits = {"mango", "berry", "banana", "apple"}
addFruits = {"cherry", "apple"}
fruits.update(addFruits)
print(fruits)

removeFruits = fruits.discard("mango")
print(fruits)
