x = lambda a: a + 1
print("The result of lamda", x(11))

# addition
y = lambda a, b, c: a + b + c
print("addition of abc ", y(2, 3, 4))

# multiplication
z = lambda a, b, c: a * b * c
print("multiplication of abc", z(3, 4, 5))


# using unknown number
def unknownFunction(n):
    return lambda a: a * n  # n is unknown


mulFunction = unknownFunction(5)
print("Using the unknown number", mulFunction(5))

# using the map
myList = [3, 4, 2, 5, 7, 9]
myNewList = list(map(lambda a: a * 2, myList))
print("using map with lamda", myNewList)
