import FreeSimpleGUI as sg
import time
from functions import read_todos, write_todos

# Error handling for importing module

sg.theme('Black')  # Changing the theme of the application

# Live clock component
clock = sg.Text('', key='clock')

# Defining the layout
label = sg.Text('Type in a to-do:')
input_box = sg.InputText(tooltip='Enter todo', key='todo', size=(40, 1))
add_button = sg.Button('Add', size=(10, 1))

list_box = sg.Listbox(values=read_todos(), key='todos', enable_events=True, size=(40, 10))

# Buttons beside the list box, aligned vertically
edit_button = sg.Button('Edit', size=(10, 1))
complete_button = sg.Button('Complete', size=(10, 1))

# Exit button
exit_button = sg.Button('Exit', size=(10, 1))

# Window layout
layout = [
    [clock],
    [label],
    [input_box, add_button],
    [list_box, sg.Column([[edit_button], [complete_button], [exit_button]])],
    # Buttons aligned vertically next to the listbox
]

# Creating the window
window = sg.Window('My To-Do App', layout, font=('Helvetica', 15), finalize=True)

while True:

    # Update the clock every second
    event, values = window.read(timeout=1000)
    # window['clock'].update(time.strftime("%Y-%m-%d %H:%M:%S"))

    if event == sg.WIN_CLOSED or event == "Exit":
        break
    # Update the clock only if the window is still open
    if window:
        window['clock'].update(time.strftime("%Y-%m-%d %H:%M:%S"))

    match event:
        case 'Add':
            todos = read_todos()
            new_todo = values['todo'].capitalize().strip()

            if not new_todo:
                sg.popup("To-Do cannot be empty, Please Add a todo!")
                continue

            todos.append(new_todo + '\n')
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].capitalize().strip()

                if not new_todo:
                    sg.popup("To-Do cannot be empty, Please enter a Todo!")
                    continue

                todos = read_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select a to-do to edit.")

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = read_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select a to-do to complete.")

        case 'todos':
            window['todo'].update(value=values['todos'][0])

window.close()
