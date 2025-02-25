import os
import FreeSimpleGUI as sg
import ToDoFunctions as ftns
import time

clock = sg.Button("time")
clock_display = sg.Text(" ", key="clock")

prompt = sg.Text("Type in a To Do item: ")
theme = sg.theme("GreenTan")

#creating the 'Add' functionality of application
input_box = sg.InputText(tooltip="Enter a todo item", key='todo_entry')
add_button = sg.Button("Add")

#creating elements for the GUI to display todo items, will add edit button on the side
todo_display = sg.Listbox(ftns.get_todos(),
                          size= (45,10),
                          key='todo_lbox',
                          enable_events=True)

#creating Edit button
edit_button = sg.Button("Edit")

#creating Complete button
complete_button = sg.Button("Complete")

#exit button
exit_button = sg.Button("Exit")

#creating the window object that creates the window of the web gui for the application
window = sg.Window('To-Do List Application', 
                   layout=[ [clock, clock_display],
                            [prompt],
                            [input_box],
                            [add_button, edit_button, complete_button],
                            [todo_display],
                            [exit_button]],
                    font=('Helvetica', 15))

while True:
    event, value = window.read(timeout=15)
    print(event)
    print(value)

    #Creates an error when exiting out of GUI box
    # window["clock"].update("no time")
    # window["clock"].update(time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        
        case 'Add':
            todo_list = ftns.get_todos()
            new_todo = value['todo_entry'] + "\n"
            todo_list.append(new_todo)
            ftns.write_todos(todo_list)

            #Updates the window gui list box element with the new todo list
            window['todo_lbox'].update(values=todo_list)
        

        case 'Edit':
            try:
                todo_list = ftns.get_todos()
                old_todo = value['todo_lbox'][0]
                new_todo = value['todo_entry']+"\n"

                # old_todo = old_todo.strip('\n')

                index = todo_list.index(old_todo)
                todo_list[index] = new_todo

                ftns.write_todos(todo_list)

                #Updates the window gui list box element with the new todo list
                window['todo_lbox'].update(values=todo_list)
            
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
            
        case 'time':
            window['clock'].update(time.strftime("%b %d, %Y %H:%M:%S"))
        

        case 'Complete':
            try:
                todo_list = ftns.get_todos()
                removed_todo = value['todo_lbox'][0]
                index = todo_list.index(removed_todo)
                todo_list.pop(index)

                ftns.write_todos(todo_list)
                window['todo_lbox'].update(values=todo_list)
            
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))

        case 'todo_lbox':
            window['todo_entry'].update(value=value['todo_lbox'][0])
        
        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break   

window.close()


