import json
import os

def genarate_diff(file_path1, file_path2, format='stylish'):
    path1 = os.path.abspath(file_path1)
    path2 = os.path.abspath(file_path2)
    data1 = json.load(open(path1))
    data2 = json.load(open(path2))
    return f"File1: {data1}\nFile2: {data2}"
