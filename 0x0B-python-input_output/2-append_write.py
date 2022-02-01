#!/usr/bin/python3
"""
The module define the function 'append_write()'
"""


def append_write(filename="", text=""):
    """
    The function appends a string at the end of a text file and
    returns the number of charaters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
