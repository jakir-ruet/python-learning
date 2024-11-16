g = "this is global variable"


def my_function():
    global g
    g = g + "add text"
    print(g)


my_function()
print(g)
