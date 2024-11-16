# for loop with break and else
for i in range(6):
   if i == 3:
      print("break the loop")
      break
else:
   print("not printed nothing")

numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
   if num == 7:
      print("6! is found")
else:
   print("6 not found")