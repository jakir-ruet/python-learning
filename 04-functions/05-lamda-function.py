greeting = lambda name: print("Hello", name)
greeting("Jakir")

x = lambda a: a + 1
print("The result of lamda", x(11))

# addition
y = lambda a, b, c: a + b + c
print("addition of abc ", y(2, 3, 4))

# multiplication
z = lambda a, b, c: a * b * c
print("multiplication of abc", z(3, 4, 5))

sumIndex = lambda *p: p[0] + p[1] + p[2] + p[3]
print("The summation by index", sumIndex(3, 4, 5, 6))

# see output without assigning its variable
lmWValue = (lambda x: x * x)(5)
print("without assigning its variable", lmWValue)

myList = [1, 2, 3, 4, 5, 6]
myNewList = list(map(lambda a: a * 2, myList))
print("Finding the sq value of list ", myNewList)


# using unknown number
def unknown_function(n):
    return lambda a: a * n  # n is unknown


mulFunction = unknown_function(5)
print("Using the unknown number", mulFunction(5))

# using the map
myList = [3, 4, 2, 5, 7, 9]
myNewList = list(map(lambda a: a * 2, myList))
print("using map with lamda", myNewList)
