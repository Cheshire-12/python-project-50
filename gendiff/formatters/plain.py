def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)

def format_plain(diff_tree, path=''):
    lines = []
    for node in diff_tree:
        key = node['key']
        current_path = f"{path}{key}"
        if node['type'] == 'nested':
            children = format_plain(node['children'], f"{current_path}.")
            lines.append(children)
        elif node['type'] == 'unchanged':
            continue
        elif node['type'] == 'changed':
            old_value = stringify(node['old_value'])
            new_value = stringify(node['new_value'])
            lines.append(f"Property '{current_path}' was updated. "
                         f"From {old_value} to {new_value}")
        elif node['type'] == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node['type'] == 'added':
            value = stringify(node['value'])
            lines.append(f"Property '{current_path}' was added with value: {value}")
    return "\n".join(lines)