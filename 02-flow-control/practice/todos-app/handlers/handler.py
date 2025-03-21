import json
import os


def handleUser():
    todos = []
    db_path = os.getenv("DB_PATH")

    # Getting data from json file
    with open(db_path, "r") as file:
        dt = file.read()
        todos = json.loads(dt)

    while True:
        user_action = input("Type add, show, edit, exit ").strip()
        match user_action:
            case "add":
                todo = input("add here: ")
                todos.append(todo)
            case "readall":
                for i, item in enumerate(todos, start=1):
                    print(i, item)
            case "edit":
                i = int(input("edit index: ")) - 1
                todo = input("edit with: ")
                todos[i] = todo
            case "exit":
                print("Exit.")

                # Writing data to json file
                with open(db_path, "w") as file:
                    file.write(json.dumps(todos))
                break
