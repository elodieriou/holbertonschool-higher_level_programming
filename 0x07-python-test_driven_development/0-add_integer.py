#!/usr/bin/python3
"""
The function add_integer.
"""


def add_integer(a, b=98):
    """
    The function adds 2 integers.

    Args:
        - a (int or float):
            . must an integer or float
            . if it's a float, caste to integers
        - b (int or float):
            . initialize to 98
            . must an integer or float
            . if it's a float, caste to integers

    Return:
        the addition of a and b
    """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    elif type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
