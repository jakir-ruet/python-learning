# and, or, not

# Precedence
# not > and > or

a = 5
b = 10

if a > 0 and b > 0:
    print("Both a and b are positive.")
else:
    print("At least one of a or b is non-positive.")


if a > 0 or b > 0:
    print("At least one of a or b is positive.")
else:
    print("Both a and b are non-positive.")

if not a < 5:
    print("x is not less than 5.")
else:
    print("x is less than 5.")