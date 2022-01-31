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
