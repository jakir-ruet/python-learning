
# String formatting in Python allows you to dynamically embed variables or expressions into strings. Python offers several ways to format strings, each with its own style and features.

name = "Alice"
age = 25
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)

result = f"5 + 3 = {5 + 3}"
print(result)

value = 123.45678
formatted = f"{value:.2f}"  # Round to 2 decimal places
print(formatted)

name = "Dana"
age = 35
greeting = "Hello, %s! You are %d years old." % (name, age)
print(greeting)
