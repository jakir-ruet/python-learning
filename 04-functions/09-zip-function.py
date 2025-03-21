# The zip() function combines multiple iterables (like lists, tuples, or dictionaries) into a single iterable of tuples, where elements at the same index are paired together.
from itertools import zip_longest


emp_name = ["Fahmid", "Ahad", "Jakir"]
dept_name = ["Admin Department", "R & D Department", "System Development"]

zipped = zip(emp_name, dept_name)
print(zipped)
print(list(zipped))

# using loop
for name, dept in zip(emp_name, dept_name):
   print(f"{emp_name}, {dept_name}")

# handling unequal length
std_name = ["Fahmid", "Ahad", "Jakir", "Rahim"]
std_class = ["Class One", "Class Two", "Class Three"]
print(list(zip(std_name, std_class)))

# or using itertools
print(list(zip_longest(std_name, std_class, fillvalue='Not Found')))