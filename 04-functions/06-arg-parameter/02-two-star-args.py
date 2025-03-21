# using **arg argument, it will receive a dictionary of arguments
# # using **arg argument, it will receive agrument as my wise.


def my_function(country="Bangladesh"):
    print("I am from ", country)


my_function("USA")
my_function()
my_function("UK")
my_function("Pakistan")


# using the **agrs that is received the dictionary
def my_argument_function(**student):
    print("Father name ", student["father"])


my_argument_function(name="John", father="sammy Ahmed")
