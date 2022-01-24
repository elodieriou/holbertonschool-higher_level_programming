#!/usr/bin/python3
"""
The function that prints a square with the character #.
"""
def print_square(size):
    """
    The function prints a square with the character #

    Args:
        - size (int):
            . is the size length of the square
            . must be an integer
            . if size is less than 0, raise a ValueError
            . if size is a float and is less than 0, raise a TypeError

    Return:
        Nothing
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for row in range(size):
            for column in range(size):
                print("#", end="")
            print("")