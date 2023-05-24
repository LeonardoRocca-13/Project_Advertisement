import os


def get_path() -> str:
    path: str = os.path.dirname(os.path.abspath(__file__))
    # going up to the parent directory (main directory)
    path = os.path.dirname(os.path.dirname(path))

    return path
