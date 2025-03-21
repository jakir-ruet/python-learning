num = int(input('Enter the number = '))

isPrime = False
if num >= 2:
    for i in range(2, num):
        if num % i == 0:
            isPrime = True
            break
if isPrime:
    print(num, 'is not a prime number')
elif num == 0 or num == 1:
    print(num, 'is neither prime nor composite')
elif num < 0:
    print(num, 'is negative number')

else:
    print(num, 'is a prime number')
