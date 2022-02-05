#!/usr/bin/python3
"""
The module define the class Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The class Square define:
        * Class constructor: def __init__(self, size, x=0, y=0, id=None)
        * Public getter and setter size:
            . no new attributes must be created
            . width and height must be assigned to the value of size
            . width, height, x, and y must inherit from Rectangle
        * Public method def update(self, *args, **kwargs)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        The initialization method:
            - call super class with id, x, y, width, height
        Args:
            - __size (int)
            - __x (int)
            - __y (int)
            - id (int)
        """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """
        The update method assigns attributes.
        Args:
            - *args: no_keyword-argument
            - **kwargs: key-worked argument like a dictionary key/value
        """
        my_attrs = ['id', 'size', 'x', 'y']

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for i in range(len(args)):
                setattr(self, my_attrs[i], args[i])

    def to_dictionary(self):
        """
        The to_dictionary method returns the dictionary representation of a
        Square
        """
        s = self.width
        x = self.x
        y = self.y
        i = self.id
        return {'id': i, 'x': x, 'size': s, 'y': y}

    def __str__(self):
        """
        The __str__ method return the information to the great format.
        """
        i = self.id
        x = self.x
        y = self.y
        size = self.width
        return "[Square] ({}) {}/{} - {}".format(i, x, y, size)

    @property
    def size(self):
        """
        The public getter method for the private instance attribute of size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        The public setter method for the private instance attribute of width.
        Args:
            - value (int): the value of width and height
        """
        self.width = value
        self.height = value
