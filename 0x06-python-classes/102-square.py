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

- Square instance can answer to comparators: ==, !=, >, >=, < and <= based on
  the square area
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
        The area method is a public instance.
        Return the current square area
        """
        return self.__size ** 2

    def __lt__(self, other):
        """Rich comparison method compares if size < other."""
        if isinstance(other, Square):
            return self.__size ** 2 < other.__size ** 2

    def __le__(self, other):
        """Rich comparison method compares if size <= other."""
        if isinstance(other, Square):
            return self.__size ** 2 <= other.__size ** 2

    def __eq__(self, other):
        """Rich comparison method compares if size == other."""
        if isinstance(other, Square):
            return self.__size ** 2 == other.__size ** 2

    def __ne__(self, other):
        """Rich comparison method compares if size != other."""
        if isinstance(other, Square):
            return self.__size ** 2 != other.__size ** 2

    def __gt__(self, other):
        """Rich comparison method compares if size > other."""
        if isinstance(other, Square):
            return self.__size ** 2 > other.__size ** 2

    def __ge__(self, other):
        """Rich comparison method compares if size >= other."""
        if isinstance(other, Square):
            return self.__size ** 2 >= other.__size ** 2
