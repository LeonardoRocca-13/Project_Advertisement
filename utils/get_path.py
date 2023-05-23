import os


def get_path():
    path = os.path.dirname(os.path.abspath(__file__))
    # going up to the parent directory (main directory)
    path = os.path.dirname(path)

    return path
