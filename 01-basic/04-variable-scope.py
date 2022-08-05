# local scope

def localScopeFunction():
    p = 350
    print('This is local scope', p)


localScopeFunction()


def parentFunction():
    q = 450

    def childFunction():
        print('This is the child function =', q)
    childFunction()
    print('This is local scope out of child function take from parent ', q)


parentFunction()


# global scope
a = 350


def globalScopeFunction():
    print('output of global scope ', a)


globalScopeFunction()

print('output of global scope after object ', a)


# If you need to create a global variable,
# but are stuck in the local scope, you can use the global keyword.

b = 650


def usingGlobalFunction():
    global b
    b = 550
    print('using global in function', b)


usingGlobalFunction()

print('using global keyword after object', b)
