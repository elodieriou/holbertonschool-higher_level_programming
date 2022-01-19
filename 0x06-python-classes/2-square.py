#!/usr/bin/python3
"""
Class Square tant defines a square:

- Size : Private instance attribute
- Instantiation with size: def __inti__(self, size=0)
  * size must be an integer, otherwise raise a TypeError exception with the
    message size must be an integer
  * if size is less than 0, raise a ValueError exception with the message size
    must be >= 0
"""


class Square:
    """ The class Square define a square."""

    def __init__(self, size=0):
        """
        The __init__ method is used. This method run as soon as an object of
        a classe is instantiated (= created).

        Args:
        - size (int): the size of the square, must be an integer

        Attribute:
        - __size: the size is a private attribute (that means the acces to
        variable size is restricted)
        """

        self.__size = size

        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
