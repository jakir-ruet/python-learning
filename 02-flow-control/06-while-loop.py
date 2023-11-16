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

# nested loop
num_parent_loop = 1
while num_parent_loop <= 3:
    num_child_loop = 1
    while num_child_loop <= 5:
        print("Parent value: ", num_parent_loop, "-", "Child value: ", num_child_loop)
        num_child_loop += 1
    print("Child loop end here")
    num_parent_loop += 1
print("Parent loop end here")
