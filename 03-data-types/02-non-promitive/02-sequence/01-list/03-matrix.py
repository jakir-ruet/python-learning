mymatrix = [
   [2, 4, 3],
   [3, 2, 1],
   [4, 5, 2]
]

# accessing to matrix
print(mymatrix[0][1])

# here considering as element using index
print(mymatrix[0])

# iterating over the matrix
for row in mymatrix:
   for element in row:
      print(element, end=" ")
   print(element)