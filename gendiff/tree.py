def build_diff_tree(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_tree = []
    for key in keys:
        if key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                children = build_diff_tree(data1[key], data2[key])
                diff_tree.append({
                    'key': key,
                    'type': 'nested',
                    'children': children
                })
            elif data1[key] == data2[key]:
                diff_tree.append({
                    'key': key,
                    'type': 'unchanged',
                    'value': data1[key]
                })
            else:
                diff_tree.append({
                    'key': key,
                    'type': 'changed',
                    'old_value': data1[key],
                    'new_value': data2[key]
                })
        elif key in data1:
            diff_tree.append({
                'key': key,
                'type': 'removed',
                'value': data1[key]
            })
        else:
            diff_tree.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })
    return diff_tree