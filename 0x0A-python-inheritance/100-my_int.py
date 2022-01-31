#!/usr/bin/python3
"""Create a class MyInt that inherits from int"""


class MyInt(int):
    """The class MyInt is a rebel, == and != operators are invented"""

    def __init__(self, other):
        """The initialize method"""
        self.__other = other

    def __eq__(self, other):
        """The equal method return non-equal value"""
        return self.__other != self.__other

    def __ne__(self, other):
        """The non-equal method return equal value"""
        return self.__other == self.__other
