import os
import FreeSimpleGUI as sg
import ToDoFunctions as ftns

prompt = sg.Text("Type in a To Do item: ")

#creating the 'Add' functionality of application
input_box = sg.InputText(tooltip="Enter a todo item", key='todo_entry')
add_button = sg.Button("Add")

#creating elements for the GUI to display todo items, will add edit button on the side
todo_display = sg.Listbox(ftns.get_todos(),
                          size= (30,70),
                          key='todo_lbox',
                          enable_events=True)

#creating Edit button
edit_button = sg.Button("Edit")

#creating Complete button
complete_button = sg.Button("Complete")

#creating the window object that creates the window of the web gui for the application
window = sg.Window('My To Do App', 
                   layout=[[prompt],
                            [input_box],
                            [add_button, edit_button, complete_button],
                            [todo_display]],
                    font=('Helvetica', 20),
                    size=(400,600))

while True:
    event, value = window.read()
    print(event)
    print(value)

    match event:

        case 'Add':
            todo_list = ftns.get_todos()
            new_todo = value['todo_entry'] + "\n"
            todo_list.append(new_todo)
            ftns.write_todos(todo_list)

            #Updates the window gui list box element with the new todo list
            window['todo_lbox'].update(values=todo_list)
        

        case 'Edit':
            todo_list = ftns.get_todos()
            old_todo = value['todo_lbox'][0]
            new_todo = value['todo_entry']+"\n"

            # old_todo = old_todo.strip('\n')

            index = todo_list.index(old_todo)
            todo_list[index] = new_todo

            ftns.write_todos(todo_list)

            #Updates the window gui list box element with the new todo list
            window['todo_lbox'].update(values=todo_list)
        

        case 'Complete':
            todo_list = ftns.get_todos()
            removed_todo = value['todo_lbox'][0]
            index = todo_list.index(removed_todo)
            todo_list.pop(index)

            ftns.write_todos(todo_list)
            window['todo_lbox'].update(values=todo_list)

        case 'todo_lbox':
            window['todo_entry'].update(value=value['todo_lbox'][0])

        case sg.WIN_CLOSED:
            break
        

window.close()


