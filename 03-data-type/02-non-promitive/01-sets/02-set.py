# set operation are union, intresection, subtraction and so on
# union set
a = {3, 2, 4}
b = {8, 3, 9}

print("using pipe sign (|) ", a | b)
print("using union function ", a.union(b))

# intersection
print("using ampersand sign (&) ", a & b)
print("using intersection function ", a.intersection(b))

# difference
print("using minus sign (-) ", a - b)
print("using difference function ", a.difference(b))
