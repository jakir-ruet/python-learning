# If any function call itself then its call recursion
def myRecursion():
   print("Hello, Recursion")
   # Calling the function
   myRecursion()

# Declare the function here
myRecursion()
# After 1000 call it will give error, due recursion limit is 1000.