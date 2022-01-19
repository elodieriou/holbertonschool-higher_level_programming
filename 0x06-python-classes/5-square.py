#!/usr/bin/python3
"""
Class Square tant defines a square:

- Private instance attribute: size
  * property def size(self): to retrieve it
  * property setter def size(self, value): to set it:
    . size must be an integer, otherwise raise a TypeError exception with the
      message size must be an integer
    . f size is less than 0, raise a ValueError exception with the message size
      must be >= 0
- Instantiation with size: def __inti__(self, size=0)
  * size must be an integer, otherwise raise a TypeError exception with the
    message size must be an integer
  * if size is less than 0, raise a ValueError exception with the message size
    must be >= 0
- Public instance methode: def area(self). This method returns the current
  square area
- Public instance method: def my_print(self): that prints in stdout the square
  with the character #:
  * if size is equal to 0, print an empty line
"""


class Square:
    """ The class Square define a square."""

    def __init__(self, size=0):
        """
        The __init__ method is used. This method run as soon as an object of
        a classe is instantiated (= created).

        Args:
        - size (int): the size of the square, must be an integer

        Attribute:
        - __size: the size is a private attribute (that means the acces to
        variable size is restricted)
        """

        self.__size = size

        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """
        @property method retrieve the data.
        Return the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        @size.setter method change the data.

        Args:
        - value (int): the size of the square, must be an integer
        """
        self.__size = value
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """
        The area method returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        The my_print method prints in stdout the square with '#'
        """
        if self.__size == 0:
            print("")
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print("")
