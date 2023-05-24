# from main_app_functions import get_todos, write_todos]
# from folder . import file (if its in another folder)
import time
import main_app_functions

now = time.strftime("%b %d, %Y %H:%M:%S")
print("it is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):  #include the most popular cases first as the interprutter goes sequentially from the top.
        todo = user_action[4:]

        todos = main_app_functions.get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = main_app_functions.get_todos()

        #  new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1

            todos = main_app_functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            main_app_functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid, please enter a number instead. ')
            continue

    elif user_action.startswith("complete"):
        try:
            number = float(user_action[9:]) - 1

            todos = main_app_functions.get_todos()

            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            main_app_functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from your list"
            print(message)
        except IndexError:
            print('Your command is not valid, please enter a number instead. ')
            continue

    elif 'exit' in user_action:
        break
    else:
        print('Print command is not valid.')

print("Bye!!")