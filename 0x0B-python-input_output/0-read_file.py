#!/usr/bin/python3
"""
The module define the function 'red_file()'
"""


def read_file(filename=""):
    """
    The function reads a text file and prints it to stdout.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print("{}".format(f.read()))
