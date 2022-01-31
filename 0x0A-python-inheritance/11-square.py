#!/usr/bin/python3
"""
The module define the class BaseGeometry:
* Public instance method: def area(self): that raises an Exception with
  the message area() is not implemented
* Public instance method: def integer_validator(self, name, value): that
  validates value:
    . you can assume name is always a string
    . if value is not an integer: raise a TypeError exception, with the
      message <name> must be an integer
    . if value is less or equal to 0: raise a ValueError exception with the
      message <name> must be greater than 0

The module define a subclass Rectangle inherits from BaseGeometry:
    * Instantiation with width and height: def __init__(self, width, height):
        . width and height must be private. No getter or setter
        . width and height must be positive integers, validated by
          integer_validator

The module define a subclass Square inherits from Rectangle inherits
from BaseGeometry:
    * Instantiation with size: def __init__(self, size)::
        . size must be private. No getter or setter
        . size must be a positive integer, validated by integer_validator
    * the area() method must be implemented
    * print() should print, and str() should return, the square description:
      [Square] <width>/<height>
"""


class BaseGeometry:
    """
    The class BaseGeometry define:
        * Public instance method: def area(self)
        * Public instance method: def integer_validator(self, name, value)
    """
    def area(self):
        """
        The method area define:
            * raises an Exception with the message area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        The method integer_validator define:

        Args:
            - name (str): is always a string
            - value (int):
                . if is not an integer, raise TypeError
                . if is less or equal to 0, raise ValueError
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


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
        The initialization method of the class Rectangle.

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


class Square(Rectangle):
    """
    The class Square define:
        * Instantiation with size: def __init__(self, size)
        * print() should print, and str() should return, the square description:
          [Square] <width>/<height>
    """
    def __init__(self, size):
        """
        The initialization method of class Square.

        Args:
            - __size (int, private)
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        The method __str__ print and return the string representation of main.
        """
        w = self.__size
        h = self.__size
        return "[Square] {:d}/{:d}".format(w, h)
