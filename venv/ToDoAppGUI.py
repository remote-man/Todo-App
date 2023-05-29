import main_app_functions
import PySimpleGUI as sg
import time

sg.theme("DarkTeal11")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
import PySimpleGUI as sg
add_button = sg.Button("Add")
list_box = sg.Listbox(values=main_app_functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


layout=[[clock], [label],
       [input_box, add_button],
       [list_box, edit_button, complete_button],
       [exit_button]]

window = sg.Window('My To-do App',  #each list is a new line
                   layout= layout, font=('Helvetica', 14))

while True:
    event, values = window.read(timeout=20)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = main_app_functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            main_app_functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = main_app_functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                main_app_functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item to edit first", font= ("Helvetica, 14"))

        case "Complete":
            try:
                todos_to_complete = values['todos'][0]
                todos = main_app_functions.get_todos()
                todos.remove(todos_to_complete)
                main_app_functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item to complete.",  font= ("Helvetica, 14"))

        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
