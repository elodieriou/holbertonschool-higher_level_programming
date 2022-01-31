#!/usr/bin/python3
"""
The module define a subclass Square inherits from Rectangle inherits
from BaseGeometry:
    * Instantiation with size: def __init__(self, size)::
        . size must be private. No getter or setter
        . size must be a positive integer, validated by integer_validator
    * the area() method must be implemented
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The class Square define:
        * Instantiation with size: def __init__(self, size)
        * the area() method must be implemented
    """
    def __init__(self, size):
        """
        The initialization method of class Square.

        Args:
            - __size (int, private)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        The method that compute the area of a square.
        """
        return self.__size ** 2
