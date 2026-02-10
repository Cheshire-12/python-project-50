import json
import os

import yaml


def load_file(file_path):
    _, extension = os.path.splitext(file_path)
    with open(file_path) as file:
        if extension in '.json':
            return json.load(file)
        elif extension in ['.yaml', '.yml']:
            return yaml.safe_load(file)
    raise ValueError(f"Unsupported file format: {extension}")