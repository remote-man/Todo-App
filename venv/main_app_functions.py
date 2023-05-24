FILEPATH = "todos.txt"


def get_todos(filepath="FILEPATH"):
    """Raad text file amd return a list of to-do items."""
    with open(filepath, 'r') as file:
        todos = file.readlines()  # no need to use.close()
    return todos


def write_todos(todos_arg, filepath="FILEPATH"): # AS the filepath has been included in this function, it has beem
    """Open the text file amd write the list of to-do items given as arguemnets. """
    with open(filepath, 'w') as file:              # removed from the call below.
        file.writelines(todos_arg)


if __name__ == "__main__":  # this seciton is only executed when this file is executed as the main file, not when
    print("Hello")          # it is called by the MainToDoApp
    print(get_todos())