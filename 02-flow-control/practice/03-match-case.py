todos = []
while True:
    user_action = input("Type add, show, edit or exit ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter the a todo ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            print("Got It")
        case "exit":
            break
