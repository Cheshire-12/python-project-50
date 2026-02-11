import os

from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.loader import load_file
from gendiff.tree import build_diff_tree


def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)
        

def generate_diff(file_path1, file_path2, format='stylish') -> str:
    path1 = os.path.abspath(file_path1)
    path2 = os.path.abspath(file_path2)
    
    data1 = load_file(path1)
    data2 = load_file(path2)
    diff_tree = build_diff_tree(data1, data2)
    
    if format == 'stylish':
        return format_stylish(diff_tree)

    if format == 'plain':
        return format_plain(diff_tree)
    raise ValueError(f"Unknown format: {format}")