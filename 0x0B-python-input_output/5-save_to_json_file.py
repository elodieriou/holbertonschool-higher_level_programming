#!/usr/bin/python3
"""
The module define the function 'save_to_json_file()'
"""
import json


def save_to_json_file(my_obj, filename):
    """
    The function writes an Object to a text filen using a JSON representation.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
