import os

def setup_file_path(folder, file):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(script_dir)
    relative_path = os.path.join(folder, file)
    file_path = os.path.join(parent_dir, relative_path)
    return file_path

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data.split('\n')
