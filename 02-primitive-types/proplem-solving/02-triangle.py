import math
a = int(input('Enter the value of A = '))
b = int(input('Enter the value of B = '))
c = int(input('Enter the value of C = '))

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print('the area = ', area)
