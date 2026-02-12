import os

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.loader import load_file
from gendiff.tree import build_diff_tree

FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json,
}


def generate_diff(file_path1, file_path2, format='stylish') -> str:
    path1 = os.path.abspath(file_path1)
    path2 = os.path.abspath(file_path2)
    
    data1 = load_file(path1)
    data2 = load_file(path2)
    diff_tree = build_diff_tree(data1, data2)
    
    if format not in FORMATTERS:
        raise ValueError(f"Unsupported format: {format}")
    
    formatter = FORMATTERS[format]
    return formatter(diff_tree)