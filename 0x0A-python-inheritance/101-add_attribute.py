#!/usr/bin/python3
"""
The module define the function 'add_attribute()'
"""


def add_attribute(obj, key, value):
    """
    The function adds a new attribute to an object if it's possible.
    Args:
        - obj: the name of the object instance
        - key (str): the attribute name
        - value: the value to set the name attribute to
    """
    if hasattr(obj, '__dict__') is False:
        raise TypeError('can\'t add new attribute')
    else:
        setattr(obj, key, value)
