num_loop = [1, 2, "Jakir", 4.90, 5, 6, 7, 8, 9]
i = 0

# using while loop
while i < len(num_loop):
    print("using while loop", num_loop[i])
    i += 1

# using while loop
for i in num_loop:
    print("using for loop", i)

# summation
var_sum = [3, 4, 2, 5, 7, 6, 8, 9]
my_sum = 0
for i in var_sum:
    my_sum += i
    print("Summation= ", my_sum)

# checking the largest number
my_largest = 0
for i in var_sum:
    if i > my_largest:
        my_largest = i
print("The largest value= ", my_largest)
