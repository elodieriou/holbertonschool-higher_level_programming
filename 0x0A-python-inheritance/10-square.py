#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
"""


Rectangle = __import__('9-rectangle').Rectangle

""" create a class square of inheritance from Rectangle"""


class Square(Rectangle):
    """ defined a square of size "size by size" """

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

        """function that compute the area of the square"""

    def area(self):
        return self.__size ** 2
