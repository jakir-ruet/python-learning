todos = []
while True:
    user_action = input(
        "Enter command (add, show, showall, edit, exit) ").strip()
    match user_action:
        case "add":
            todo = input("add here: ")
            todos.append(todo)
        case "showall":
            for i, item in enumerate(todos, start=1):
                print(i, item)
        case "show":
            i = int(input("serial no: ")) - 1
            print(i + 1, todos[i])
        case "edit":
            i = int(input("edit index: ")) - 1
            todo = input("edit with: ")
            todos[i] = todo
        case "exit":
            print("Got It")
            break
