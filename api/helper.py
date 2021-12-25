import os

#param path: relative path from project root dir
def get_absolute_path(path: str) -> str:
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, '../' + path)
