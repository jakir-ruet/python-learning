#using **arg argument, it will receive a dictionary of arguments
def myFunction(country = "Bangladesh"):
   print("I am from ", country)
myFunction("USA")
myFunction()
myFunction("UK")
myFunction("Pakistan")

#using the **agrs that is receive the dictionary
def myArgumentFunction(**student):
   print("Father name ", student["father"])
myArgumentFunction(name = "John", father = "Samim Ahmed")