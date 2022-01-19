#!/usr/bin/python3
"""
Class Square tant defines a square:

- Size : Private instance attribute
- Instantiation with size (no type/value verification)
"""


class Square:
    """ The class Square define a square."""

    def __init__(self, size):
        """
        The __init__ method is used. This method run as soon as an object of
        a classe is instantiated (= created).

        Args:
        - size: the size of the square

        Attribute:
        - __size: the size is a private attribute (that means the acces to
        variable size is restricted)
        """

        self.__size = size
