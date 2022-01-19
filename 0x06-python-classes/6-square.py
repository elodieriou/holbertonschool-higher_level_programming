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

- Private instance attribute: position
  * property def position(self): to retrieve it
  * property setter def position(self, value): to set it:
    . position must be a tuple of 2 positive integers, otherwise raise a
      TypeError exception with the message 'position must be a tuple of 2
      positive integers'

- Instantiation with size and optional position: def __inti__(self, size=0,
  position=(0, 0))
  * size must be an integer, otherwise raise a TypeError exception with the
    message size must be an integer
  * if size is less than 0, raise a ValueError exception with the message size
    must be >= 0
  * position must be a tuple of 2 positive integers, otherwise raise a
    TypeError exception with the message 'position must be a tuple of 2
    positive integers'

- Public instance methode: def area(self). This method returns the current
  square area

- Public instance method: def my_print(self): that prints in stdout the square
  with the character #:
  * if size is equal to 0, print an empty line
  * position should be use by using space - Don’t fill lines by spaces when
    position[1] > 0
"""


class Square:
    """ The class Square define a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method is used. This method run as soon as an object of
        a classe is instantiated (= created).

        Args:
        - size (int): the size of the square, must be an integer
        - position (tuple): the position of the square, must be a tuple

        Attribute:
        - __size: the size is a private attribute (that means the acces to
        variable size is restricted)
        - __position: the position is a private attribute
        """

        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__position = position
        if isinstance(position, tuple) is False:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

    @property
    def size(self):
        """
        @property size method retrieve the data.
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

    @property
    def position(self):
        """
        @property position method return the position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        @position.setter method change the square's position

        Args:
        - value (tuple): the position of the square, must be a tuple
          and 2 positive integers
        """
        self.__position = value

        if isinstance(value, tuple) is False:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        """
        The my_print method prints in stdout the square with '#'
        """
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                print("")
            for row in range(self.__size):
                for pos in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print("")
