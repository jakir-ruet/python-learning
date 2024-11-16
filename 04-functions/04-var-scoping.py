a = "I am global"
b = "I am also global"


def my_scoping_function():
    # here is local var
    a = "I am local"
    print("print from local ", a + " -", b)  # we get output from both local & global


my_scoping_function()
print("print from global ", a)  # we get output from only global
