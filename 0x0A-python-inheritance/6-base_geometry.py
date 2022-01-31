#!/usr/bin/python3
"""
The module define the class BaseGeometry:
* Public instance method: def area(self): that raises an Exception with
  the message area() is not implemented
"""


class BaseGeometry:
    """
    The class BaseGeometry define:
        * Public instance method: def area(self)
    """
    def area(self):
        """
        The method area define:
            * raises an Exception with the message area() is not implemented
        """
        raise Exception('area() is not implemented')
