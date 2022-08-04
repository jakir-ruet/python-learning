#making the factorial
num = 5
def factorial(a):
   if a == 1:
      return 1
   else:
      return (a * factorial(a - 1))
print("The factorial of", num, "is", factorial(num))