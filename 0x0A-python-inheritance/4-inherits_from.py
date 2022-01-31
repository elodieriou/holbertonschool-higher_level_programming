#!/usr/bin/python3
"""
The module define the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    The function inherits_from returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified class ;
    otherwise False
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
