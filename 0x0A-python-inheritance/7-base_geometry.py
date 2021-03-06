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
