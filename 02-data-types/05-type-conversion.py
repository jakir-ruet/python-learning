# Implicit Type Conversion:
# Python automatically converts one data type to another without requiring explicit instruction.
# Implicit conversion from int to float
num_int = 10
num_float = 2.5
result = num_int + num_float  # int + float → float
result = f"{num_int} + {num_float} = {result}"

print(result, type(result))

# Explicit Type Conversion:
# Explicit type conversion requires the use of built-in functions to convert between data types.

# Integer to String
num = 123
converted = str(num)
print(converted, type(converted))

# String to Integer
text = "456"
converted = int(text)
print(converted, type(converted))

# List to Tuple
my_list = [1, 2, 3]
converted = tuple(my_list)
print(converted, type(converted))

# String to List
text = "hello"
converted = list(text)
print(converted, type(converted))

