#!/usr/bin/python3
"""
Class Rectangle that define a rectangle

- Private instance attribute: width:
    * property def width(self): to retrieve it
    * property setter def width(self, value): to set it:
        . width must be an integer, otherwise raise a TypeError
          exception with the message width must be an integer
        . if width is less than 0, raise a ValueError exception with
          the message width must be >= 0

- Private instance attribute: height:
    * property def height(self): to retrieve it
    * property setter def height(self, value): to set it:
        . height must be an integer, otherwise raise a TypeError exception
          with the message height must be an integer
        . if height is less than 0, raise a ValueError exception with
          the message height must be >= 0

- Instantiation with optional width and height: def __init__(self, width=0,
  height=0):

- Public instance method: def area(self): that returns the rectangle area

- Public instance method: def perimeter(self): that returns the rectangle
  perimeter:
    * if width or height is equal to 0, perimeter is equal to 0

- print() and str() should print the rectangle with the character #:
    * if width or height is equal to 0, return an empty string

- repr() should return a string representation of the rectangle to be
  able to recreate a new instance by using eval()

- Print the message Bye rectangle... (... being 3 dots not ellipsis)
  when an instance of Rectangle is deleted

- Public class attribute number_of_instances:
    * Initialized to 0
    * Incremented during each new instance instantiation
    * Decremented during each instance deletion

"""


class Rectangle:
    """
    A class that define a rectangle.
    Initialisation of the public class attribute number_of_instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        The instance method called when a new object is created.

        Args:
            - width (int):
                . the width of a rectangle
                . must be an int
                . if width is less than 0, raise ValueError
            - height (int):
                . the height of a rectangle
                . must be an integer
                . if height is less than 0, raise ValueError

        Attribute:
            - __width: the width is a private attribute
            - __height: the height is a private attribute
            - Rectangle.number_of_instances: incremented during
              each new instance instantiation
        """
        if isinstance(width, int) is False:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        elif isinstance(height, int) is False:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')

        self.__height = height
        self.__width = width

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        This method retrieve the data of the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method set the data of the width.

        Args:
            - value (int): the width of the rectangle
        """

        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        This method retrieve the data of the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This method set the data of the height.

        Args:
            - value (int): the height of the rectangle
        """

        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Public instance area.
        Return the rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance perimeter.
        Return the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """
        The instance method that returns an 'informal' and nicely
        printable string representation of an instance.
        """
        print_rectangle = ""
        w = self.__width
        h = self.__height
        if w == 0 or h == 0:
            return print_rectangle
        else:
            for row in range(h):
                for column in range(w):
                    print_rectangle += '#'
                if row < h - 1:
                    print_rectangle += '\n'
            return print_rectangle

    def __repr__(self):
        """
        The Instance method that returns an “official” string
        representation of an instance.
        """
        w = self.__width
        h = self.__height
        return "Rectangle({:d}, {:d})".format(w, h)

    def __del__(self):
        """
        The instance method called when an instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
