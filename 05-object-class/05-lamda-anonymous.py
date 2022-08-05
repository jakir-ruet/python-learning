greet = lambda name : print('Hello', name)
greet('Jakir')

sum = lambda x, y, z : x + y + z
print('The summation =', sum(4, 5, 7))

#take any number of parameter
sumIndex = lambda *x : x[0] + x[1] + x[2] + x[3]
print('The summation by index', sumIndex(3, 4, 5, 6))

#see output without assigning its variable
lmWValue = (lambda x : x * x)(5)
print('without assigning its variable', lmWValue)

myList = [1, 2, 3, 4, 5, 6]
myNewList = list(map(lambda a : a * 2, myList))
print('Finding the sq value of list ', myNewList)
