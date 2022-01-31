#!/usr/bin/python3
"""
A function that returns the list of available attributes and methods
of an object
"""


def lookup(obj):
    """
    lookup returns a list of available attributes and methods of an object
    """
    return dir(obj)
