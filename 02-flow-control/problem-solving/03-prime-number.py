def isPrime(n):
    d = [True for i in range(n)]
    for i in range(2, n):
        d[n % i] = False
    return d[0] and n != 1


n = int(input("Enter a number: "))

if isPrime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
