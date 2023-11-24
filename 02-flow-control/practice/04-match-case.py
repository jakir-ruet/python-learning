todos = []
while True:
    user_action = input("Type add, show, edit, exit ").strip()
    match user_action:
        case "add":
            todo = input("add here: ")
            todos.append(todo)
        case "show":
            for i, item in enumerate(todos, start=1):
                print(i, item)
        case "edit":
            i = int(input("edit index: ")) - 1
            todo = input("edit with: ")
            todos[i] = todo
        case "exit":
            print("Got It")
            break
