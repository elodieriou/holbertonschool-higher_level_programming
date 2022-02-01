#!/usr/bin/python3
"""
The module define the function 'from_json_string()'
"""
import json


def from_json_string(my_str):
    """
    The function returns an object (Python data structure) represented by
    JSON string.
    """
    return json.loads(my_str)
