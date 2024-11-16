# local scope
def local_scope_function():
    p = 350
    print('This is local scope', p)

local_scope_function()
def parent_function():
    q = 450
    def child_function():
        print('This is the child function =', q)
    child_function()
    print('This is local scope out of child function take from parent ', q)
parent_function()
# global scope
a = 350

def global_scope_function():
    print('output of global scope ', a)

global_scope_function()

print('output of global scope after object ', a)

# If you need to create a global variable,
# but are stuck in the local scope, you can use the global keyword.

b = 650

def using_global_function():
    global b
    b = 550
    print('using global in function', b)

using_global_function()
print('using global keyword after object', b)

# ------------------------------------------------------
a = "I am global"
b = "I am also global"

def my_scoping_function():
    # here is local var
    a = "I am local"
    print("print from local ", a + " -", b)  # we get output from both local & global

my_scoping_function()
print("print from global ", a)  # we get output from only global
