# errors & exceptions
# syntax error
# local error
# runtime error
# exception handleing

a = int(input("enter the numerator= "))
b = int(input("enter the denominator= "))

try:
   result = a/b
except ZeroDivisionError:
   print("can't divided a number by 0")
else:
   print(result)
finally:
   print("this code block doesn't work properly")