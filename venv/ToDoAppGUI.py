import main_app_functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
import PySimpleGUI as sg
add_button = sg.Button("Add")

window = sg.Window('My To-do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = main_app_functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            main_app_functions.write_todos(todos)
        case sg.WIN_CLOSED
            break

window.close()
