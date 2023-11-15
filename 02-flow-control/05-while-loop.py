num_count_break = 1
while True:
   print(num_count_break)
   num_count_break += 1
   if num_count_break == 10:
      break

num_count_continue = 0
while num_count_continue < 10:
   num_count_continue += 1
   if num_count_continue == 5:
      continue
   print("Result ", num_count_continue)