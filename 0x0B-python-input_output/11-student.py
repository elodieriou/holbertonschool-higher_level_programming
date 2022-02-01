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
        . If attrs is a list of strings, only attribute names contained in
          this list must be retrieved.
        . Otherwise, all attributes must be retrieved
    * Public method def reload_from_json(self, json): that replaces all
      attributes of the Student instance:
        . You can assume json will always be a dictionary
        . A dictionary key will be the public attribute name
        . A dictionary value will be the value of the public attribute
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

    def to_json(self, attrs=None):
        """
        The method retrieves a dictionary representation of a Student instance.
        Args:
            - attrs (str)
                . if is a list of string, only attribute known must be
                  retrieved
        """
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for i in attrs:
            if i in self.__dict__:
                my_dict[i] = self.__dict__[i]
        return my_dict

    def reload_from_json(self, json):
        """
        The method replace all attributes of the Student instance.
        Args:
            - json (dict)
                . A dictionary key will be the public attribute name
                . A dictionary value will be the value of the public attribute
        """
        for key, value in json.items():
            self.__dict__[key] = value
