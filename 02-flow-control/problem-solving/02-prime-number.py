num = int(input("Enter a integer number: "))
isPrime = False

if num == 1:
    print(num, "neither prime nor composite number")
elif num > 1:
    # checking the prime/not
    for i in range(2, num):
        if (num % i) == 0:
            isPrime = True
            break
    # checking the prime/not
    if isPrime:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
