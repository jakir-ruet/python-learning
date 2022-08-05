# making the factorial

num = 5


def factorial(a):
    if a == 1:
        # terminate recursion
        return 1
    else:
        # recursive call
        return a * factorial(a - 1)


print("The factorial of", num, "is", factorial(num))


def countDown(n):
    print("Enter the value of n", n)
    if n == 0:
        # terminate recursion
        return
    else:
        # recursive call
        countDown(n - 1)


countDown(6)
