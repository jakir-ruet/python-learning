a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

largest = 0

if a >= b and a >= c:
    largest = a
if b >= a and b >= c:
    largest = b
if c >= a and c >= b:
    largest = c

print(largest, 'is largest number')

lowest = 0
if a <= b and a <= c:
    lowest = a
if b <= a and b <= c:
    lowest = b
if c <= a and c <= b:
    lowest = c

print(lowest, 'is lowest number')
