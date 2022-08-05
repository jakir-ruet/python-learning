# function two type 1. built in 2. user define function


def myGeneralFunction(c1, c2, c3):
    print("The youngest child is", c1)
    print("The youngest child is", c2)
    print("The youngest child is", c3)


myGeneralFunction("c1", "c2", "c3")


# using *arg argument, it will receive a tuple of arguments
def myArgsFunction(*kids):
    print("The youngest child is ", kids[1])


myArgsFunction("John", "Kite", "Sam")


# using default value of argument
def greet(name, msg="good morning"):
    print("Hello", name + ', ' + msg)


greet("john")
greet("kite", "how are you?")
