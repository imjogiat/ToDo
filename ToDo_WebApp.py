import streamlit as stlt
import ToDoFunctions as tdf

todo_list = tdf.get_todos()

def add_todo():
    new_todo = stlt.session_state["new_todo"] + "\n"
    todo_list.append(new_todo)
    tdf.write_todos(todo_list)

    
stlt.title("My To-Do List App")
stlt.subheader("Just a simple To-Do list")
stlt.write("Please select an option below: ")


for index, todo in enumerate(todo_list):
    checked_box = stlt.checkbox(todo, key=todo)

    if checked_box:
        todo_list.pop(index)
        tdf.write_todos(todo_list)
        del stlt.session_state[todo]
        stlt.rerun()

stlt.text_input("", placeholder="Add new to do item...", on_change=add_todo, key="new_todo")
