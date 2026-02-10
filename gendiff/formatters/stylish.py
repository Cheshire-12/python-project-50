def stringify(value, depth):
    if not isinstance(value, dict):
        if value is None:
            return 'null'
        if isinstance(value, bool):
            return str(value).lower()
        return str(value)
    indent = ' ' * (depth * 4)
    lines = []
    for key, val in value.items():
        lines.append(f"{indent}    {key}: {stringify(val, depth + 1)}")
        
    result = "\n".join(lines)
    return f"{{\n{result}\n{indent}}}"


def format_stylish(diff_tree, depth=1):
    indent = ' ' * ((depth - 1) * 4)
    lines = []
    for node in diff_tree:
        key = node['key']
        if node['type'] == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent}    {key}: {children}")
        elif node['type'] == 'unchanged':
            value = stringify(node['value'], depth)
            lines.append(f"{indent}    {key}: {value}")
        elif node['type'] == 'changed':
            old_value = stringify(node['old_value'], depth)
            new_value = stringify(node['new_value'], depth)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        elif node['type'] == 'removed':
            value = stringify(node['value'], depth)
            lines.append(f"{indent}  - {key}: {value}")
        elif node['type'] == 'added':
            value = stringify(node['value'], depth)
            lines.append(f"{indent}  + {key}: {value}")
    result = "\n".join(lines)
    return f"{{\n{result}\n{indent}}}"