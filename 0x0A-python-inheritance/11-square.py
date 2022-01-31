#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return
the square description: [Square] <width>/<height>
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defined a square of size "size by size" """

    """__init__ method to initialize a new instance"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """area method to compute the area of the rectangle"""

    def area(self):
        return self.__size ** 2

    """str method to print the rectangle size"""

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
