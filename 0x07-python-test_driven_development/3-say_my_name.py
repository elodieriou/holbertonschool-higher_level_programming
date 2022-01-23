#!/usr/bin/python3
"""
The function that prints My name is <first name> <last name>
"""
def say_my_name(first_name, last_name=""):
    """
    The function prints My name.

    Args:
        - first_name (str):
            . must be a string

        - last_name (str):
            . by default empty
            . must be a string

    Return:
        Nothing
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}". format(first_name, last_name))