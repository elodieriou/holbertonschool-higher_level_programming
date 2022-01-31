#!/usr/bin/python3
"""
The module define a subclass Rectangle inherits from BaseGeometry:
    * Instantiation with width and height: def __init__(self, width, height):
        . width and height must be private. No getter or setter
        . width and height must be positive integers, validated by
          integer_validator
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The class Rectangle define:
        * Private instance method: def __init__(self, width, height)
        * the area() method must be implemented
        * print() should print, and str() should return, the following
          rectangle description: [Rectangle] <width>/<height>
    """
    def __init__(self, width, height):
        """
        The initialization method.

        Args:
            - __width (int, private)
            - __height (int, private)
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        The method area define the area with width * height.
        """
        w = self.__width
        h = self.__height
        return w * h

    def __str__(self):
        """
        The method __str__ print and return the string representation of main.
        """
        w = self.__width
        h = self.__height
        return "[Rectangle] {:d}/{:d}".format(w, h)
