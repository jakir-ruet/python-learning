#A variable is only available from inside the region it is created. This is called scope.
#local scope
def localScopeFunction():
   p = 350
   print("This is local scope =", p)
localScopeFunction()

def parentFunction():
   q = 450
   def childFunction():
      print("This is local in child function =", q)
   childFunction()
   print("This local scope out of child function", q)
parentFunction()

#global scope
a = 950
def globalScopeFunction():
   print("The output of global scope in function =", a)
globalScopeFunction()
print("The output of global scope out function =", a)

print("========using the global keyword========")
#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
def globalGScopeFunction():
   global b
   b = 550
globalGScopeFunction()
print("Using the global keyword", b)

c = 560
def globalGScopeFunctionOne():
   global c
   c = 570
   globalGScopeFunctionOne()
print("Using the global keyword", c)
