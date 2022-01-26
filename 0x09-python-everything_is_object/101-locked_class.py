#!/usr/bin/python3
"""
The class LockedClass is a class Object. When called, it accepts no arguments
and returns a new featureless instance that has no instance attributes and
cannot be given any.
"""


class LockedClass(object):
    """
    The class attribute __slots__ is called. slots provide a special mechanism
    to reduce the size of objects. It is a concept of memory optimisation on
    objects.
    """
    __slots__ = 'first_name'
