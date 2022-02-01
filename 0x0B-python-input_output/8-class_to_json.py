#!/usr/bin/python3
"""
The module define the function 'class_to_json()'
"""
import json


def class_to_json(obj):
    """
    The function returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for
    JSON serialization of an object.

    The __dict__ is a dict structure that only displays attributes
    on a dictionary.
    """
    return obj.__dict__
