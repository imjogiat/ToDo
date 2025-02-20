import os
import FreeSimpleGUI as sg

prompt = sg.Text("Type in a To Do item: ")
input_box = sg.InputText(tooltip="Enter a todo item")
add_button = sg.Button("Add")

window = sg.Window('My To Do App', layout=[[prompt],[input_box, add_button]])
window.read()
window.close()


# while True:

#     # new_todo_file = open('todos.txt','x')

#     user_action = input("\nPlease enter the todo list item to add (Ex: Add To do item), or Show, Edit, Complete. Type Exit to quit.\n")
#     user_actions_list = user_action.split(sep = " ", maxsplit = 1)

#     user_action = user_actions_list[0]
#     user_action = user_action.strip()
#     user_action = user_action.title()


#     with open('todos.txt','r') as prior_todo_file:
#         todo_list = prior_todo_file.readlines()

#     match user_action:

#         case "Add":

#             todo_item = f"{user_actions_list[1]}\n"

#             # todo_item = input("Enter a to do list item:    ") + "\n"

#             # todo_item = todo_item.strip(" ")
#             todo_list.append(todo_item)

#             with open('todos.txt','w') as todofile:
#                 todofile.writelines(todo_list)

#             # print(f"{os.getcwd()}{os.sep}todos.txt")
#             #line to show a filepath of the directory where the code is being run        

#         case "Show":

#             # todo_list = [item.strip('\n') for item in todo_list]  
#             #example of list comprehension (adds time complexity)

#             print("\n To Do list:\n-----------------------------------------------")
#             for i , item in enumerate(todo_list):
#                 item.strip('\n')
#                 item = item.title()
#                 print(f"{i+1} - {item}")
#             print("\n")


#         case "Edit":
#             user_number = int(input("\nEnter the number of the list item that you wish to edit\n"))
#             item_index = user_number - 1
#             current_todo_item = todo_list[item_index]
#             print("\nyou have selected:  " + current_todo_item)

#             new_todo_item = input("\nWhat would you like to replace that to-do list item with instead?\n") + "\n"
#             todo_list[item_index] = new_todo_item

#             with open('todos.txt','w') as todofile:
#                 todofile.writelines(todo_list)

            
#         case "Complete":
#             completed_index = int(input("Please enter the item number marked as complete. This item will be removed from the To Do list.\n"))
#             to_remove = todo_list[completed_index-1].strip('\n')
#             todo_list.pop(completed_index-1)

#             with open('todos.txt','w') as todofile:
#                 todofile.writelines(todo_list)

#             print(f"The to do list item, {to_remove}, has been removed from the ToDo list")

#         case "Exit":
#             break
        
#         case _:
#             print("\nInvalid entry, please try again\n")

    
# print("\n-----------------\nGoodbye!")

# #comment