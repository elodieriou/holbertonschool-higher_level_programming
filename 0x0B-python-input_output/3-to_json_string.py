#!/usr/bin/python3
"""
The module define the function 'to_json_string()'
"""
import json


def to_json_string(my_obj):
    """
    The function returns the JSON representation of an object(string).
    """
    return json.dumps(my_obj)
