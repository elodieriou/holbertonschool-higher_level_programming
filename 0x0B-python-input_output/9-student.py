#!/usr/bin/python3
"""
The module define the class Student.
"""


class Student:
    """
    The class Student define:
    * Public instance attributes:
        . first_name
        . last_name
        . age
    * Instantiation with first_name, last_name and age
    * Public method def to_json(self): that retrieves a dictionary
      representation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        The initialization method.
        Args:
            - first_name (str)
            _ last_name (str)
            _ age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        The method retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
