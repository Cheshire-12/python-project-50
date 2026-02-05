import json
import os

def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)
        

def generate_diff(file_path1, file_path2, format='stylish') -> str:
    path1 = os.path.abspath(file_path1)
    path2 = os.path.abspath(file_path2)
    data1 = json.load(open(path1))
    data2 = json.load(open(path2))
    
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []
    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f"    {key}: {stringify(data1[key])}")
            else:
                diff.append(f"  - {key}: {stringify(data1[key])}")
                diff.append(f"  + {key}: {stringify(data2[key])}")
        elif key in data1:
            diff.append(f"  - {key}: {stringify(data1[key])}")
        else:
            diff.append(f"  + {key}: {stringify(data2[key])}")
    return "{\n" + "\n".join(diff) + "\n}"