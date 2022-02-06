#!/usr/bin/python3
"""
The module define the class Base.
"""
import os.path
import json
import csv


class Base:
    """
    The class Base define:
        * private class attribute __nb_objects = 0
        * class constructor: def __init__(self, id=None)
        * Static method def to_json_string(list_dictionaries)
        * Class method def save_to_file(cls, list_objs)
        * Static method def from_json_string(json_string)
        * Class method def create(cls, **dictionary)
        * Class method def load_from_file(cls)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The initialization method.
        Args:
            - id (int): initialize to None
                . if id is not None assign the public instance
                  attribute id with this argument value
                . if id is None, increment __nb_objects and assign
                  the new value to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        The static method returns the JSON string representation of
        list_dictionaries.
        Args:
            - list_dictionaries (list of dict)
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        The class method writes the JSON string representation of
        list_objs to a file.
        Args:
            - list_objet (list of instances inherits of Base)
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))
            else:
                my_list_dict = []
                for i in list_objs:
                    my_list_dict.append(i.to_dictionary())
                return f.write(cls.to_json_string(my_list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        The static method returns the list of the JSON string
        representation json_string.
        Args:
            - json_string (string representing a list of dictionaries)
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        The class method returns an instance with all attributes already set.
        Args:
            - **dictionary: random of args
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2, 3, 4, 5)
        elif cls.__name__ == 'Square':
            dummy = cls(1, 2, 3, 4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        The class method returns a list of instances.
        """
        filename = cls.__name__ + '.json'
        if os.path.exists(filename) is False:
            return []
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                my_list = cls.from_json_string(f.read())
                my_list_inst = []
                for i in range(len(my_list)):
                    dummy = cls.create(**my_list[i])
                    my_list_inst.append(dummy)
                return my_list_inst
