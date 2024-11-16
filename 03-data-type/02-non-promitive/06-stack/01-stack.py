a = "Hello World!"
print(type(a))
print(a)

b = "Mohamed" + 'Ali'
print(b)

c = "5" + "5"
print(c)

# d = 1 + '3' + '4' #got an error
# print(d)

print("Allah " * 5)
print(5 * '5')
# print('50' * '50') #got an error
# print('50' * 50.0) #got an error

# formatting
msg = "My score on Python: {0}, JavaScript: {1}, Java: {2}, Swift: {3}". format(6, 6.5, 5, 6)
print(msg)
message = "If x = {x} and y = {y}, then x+y = {z}".format(x = 20, y = 300, z = 20 + 300)
print(message)

# formatting using join method
print(", ".join(["Mango", "Banana", "Apple"]))
print("Hello ME".replace("ME", "World!"))

# checking the specific word in any string
print("My name is Jakie".startswith("My"))
print(" name is Jakie".startswith("My"))
print("My name is Jakie".endswith("Jakie"))
print("My name is ".endswith("Jakie"))

# uppercase & lowercase
print("My name is Jakie".upper())
print("My name is Jakie".lower())

# split the alphabet in a world
print("a, e, i, o, u".split(", "))
