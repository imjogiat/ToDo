FILE = 'todos.txt'

def get_todos(filepath=FILE):

    """Reads a (default arg) text file and returns the to-do list in that file"""
    with open(filepath,"r") as input_todos_local:
        local_todos=input_todos_local.readlines()
    return local_todos


def write_todos(todos_list, filepath=FILE):
    """writes a to-do list to a file (default arg)"""
    with open(filepath,"w") as output_todos_local:
        output_todos_local.writelines(todos_list)