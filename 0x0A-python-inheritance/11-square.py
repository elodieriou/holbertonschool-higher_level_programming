#!/usr/bin/python3
"""
The module define a subclass Square inherits from Rectangle inherits
BaseGeometry:
    * Instantiation with size: def __init__(self, size)::
        . size must be private. No getter or setter
        . size must be a positive integer, validated by integer_validator
    * the area() method must be implemented
    * print() should print, and str() should return, the square description:
      [Square] <width>/<height>
"""
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
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        The method that compute the area of a square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        The method __str__ print and return the string representation of main.
        """
        w = self.__size
        h = self.__size
        return "[Square] {:d}/{:d}".format(w, h)
