#!/usr/bin/python3
"""
The module define the class Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """
    The class Rectangle define:
        * Class constructor: def __init__(self, width, height, x=0, y=0,
          id=None)
        * Public method def area(self)
        * Public method def display(self)
        * The __str__ method
        * Public method def update(self, *args, **kwargs)
        * Public method def to_dictionary(self)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The initialization method:
            - call super class with id
        Args:
            - __width (int)
            - __height (int)
            - __x (int)
            - __y (int)
            - id (int)
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """
        The area method returns the area value of the Rectangle instance.
        """
        w = self.__width
        h = self.__height
        return w * h

    def display(self):
        """
        The display method prints in stdout the Rectangle instance with the
        character '#'.
        """
        print_rectangle = ""
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y

        if y > 0:
            for val_y in range(y):
                print_rectangle += '\n'
        for row in range(h):
            for val_x in range(x):
                print_rectangle += ' '
            for column in range(w):
                print_rectangle += '#'
            if row < h - 1:
                print_rectangle += '\n'
        print("{}".format(print_rectangle))

    def update(self, *args, **kwargs):
        """
        The update method assigns an argument to each attribute.
        Args:
            - *args: no_keyword-argument
            - **kwargs: key-worked argument like a dictionary key/value
        """
        my_attrs = ['id', 'width', 'height', 'x', 'y']

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for i in range(len(args)):
                setattr(self, my_attrs[i], args[i])

    def to_dictionary(self):
        """
        The to_dictionary method returns the dictionary representation of a
        Rectangle
        """
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        i = self.id
        return {'x': x, 'y': y, 'id': i, 'height': h, 'width': w}

    def __str__(self):
        """
        The __str__ method return the information to the great format.
        """
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        i = self.id
        return "[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h)

    @property
    def width(self):
        """
        The public getter method for the private instance attribute of width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The public setter method for the private instance attribute of width.
        Args:
            - value (int): the value of width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        The public getter method for the private instance attribute of height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The public setter method for the private instance attribute of height.
        Args:
            - value (int): the value of height
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        The public getter method for the private instance attribute of x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        The public setter method for the private instance attribute of x.
        Args:
            _ value (int): the value of x-axis
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        The public getter method for the private instance attribute of y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        The public setter method for the private instance attribute of y.
        Args:
            - value (int): the value of y-axis
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
