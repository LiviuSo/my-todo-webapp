FILE_PATH = "todos.txt"


def get_todos(filepath=FILE_PATH):
    """ Read a text file and return a list of todo items """

    # create the file if it doesn't exist
    from os import path
    if not path.exists(filepath):
        with open(filepath, 'w') as file_local:
            pass

    # read the file
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILE_PATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
