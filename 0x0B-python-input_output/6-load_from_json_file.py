#!/usr/bin/python3
"""
The module define the function 'load_from_json_file()'
"""
import json


def load_from_json_file(filename):
    """
    The function creates an Object from a 'JSON file'.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
