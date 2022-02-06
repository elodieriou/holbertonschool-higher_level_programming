#!/usr/bin/python3
"""
Add unit test for the class Base
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstance(unittest.TestCase):
    """This class tests the class Base about incrementation."""

    def test_id_integer(self):
        """Tests with id as a integer."""
        b = Base(1)
        self.assertEqual(b.id, 1)
        b = Base(12)
        self.assertEqual(b.id, 12)
        b = Base(201)
        self.assertEqual(b.id, 201)

    def test_id_neg(self):
        """Tests with id as a negative integer."""
        b = Base(-1)
        self.assertEqual(b.id, -1)
        b = Base(-12)
        self.assertEqual(b.id, -12)

    def test_id_true(self):
        """Test with id as a boolean."""
        b = Base(True)
        self.assertEqual(b.id, True)

    def test_id_string(self):
        """Test with id as a string."""
        b = Base('hello')
        self.assertEqual(b.id, 'hello')

    def test_id_tuple(self):
        """Test with id as a tuple."""
        b = Base((1, 2, 3))
        self.assertEqual(b.id, (1, 2, 3))

    def test_id_dict(self):
        """Tests with id as a dictionary."""
        b = Base({1, 2, 3})
        self.assertEqual(b.id, {1, 2, 3})
        b = Base({'name': 'holberton', 'age': 6})
        self.assertEqual(b.id, {'name': 'holberton', 'age': 6})

    def test_id_list(self):
        """Test with id as a list."""
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_incrementation(self):
        """Checks if the incrementation works."""
        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(None)
        self.assertEqual(b.id, 2)

    def tests_too_many_args(self):
        """Test with too many arguments"""
        with self.assertRaises(TypeError):
            Base(1, 1)
        with self.assertRaises(TypeError):
            Base(1, None)


class TestBaseToJsonString(unittest.TestCase):
    """
    This class tests the class Base about the method 'to_json_string()'.
    """

    def test_to_json_string_rectangle(self):
        """Tests the method with a Rectangle instance."""

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(json_dictionary, '[{"x": 2, "y": 8, "id": 1,'
                                          ' "height": 7, "width": 10}]')

    def test_to_json_string_square(self):
        """Tests the method with a Square instance."""
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(json_dictionary,
                         '[{"id": 1, "x": 2, "size": 10, "y": 1}]')

    def test_empty_list(self):
        """Test with an empty list as argument."""
        r1 = []
        list_dictionaries = Base.to_json_string(r1)
        self.assertEqual(list_dictionaries, '[]')

    def test_none(self):
        """Test with None as argument."""
        r1 = None
        list_dictionaries = Base.to_json_string(r1)
        self.assertEqual(list_dictionaries, '[]')

    def test_without_args(self):
        """Test without arguments"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_too_many_args(self):
        """Test with too many arguments"""
        with self.assertRaises(TypeError):
            Base.to_json_string([{1, 2, 3}], [{4, 5, 6}])


class TestBaseSaveToFile(unittest.TestCase):
    """
    This class test the class Base about the function 'save_to_file()'.
    """

    def test_save_to_file_rectangle(self):
        """Test with a Rectangle instance."""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_objs = ('[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, ' +
                     '{"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]')
        with open("Rectangle.json", "r", encoding='utf-8') as f:
            self.assertEqual(f.read(), list_objs)
        os.remove('Rectangle.json')

    def test_save_to_file_square(self):
        """Test with a square instance."""
        Base._Base__nb_objects = 0
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        list_objs = ('[{"id": 8, "x": 7, "size": 10, "y": 2}, ' +
                     '{"id": 1, "x": 4, "size": 2, "y": 0}]')
        with open('Square.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), list_objs)
        os.remove('Square.json')

    def test_save_to_file_none_rectangle(self):
        """Test with None as arguement."""
        Rectangle.save_to_file(None)
        list_objs = '[]'
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), list_objs)
        os.remove('Rectangle.json')

    def test_save_to_file_none_square(self):
        """Test with None as argument."""
        Square.save_to_file(None)
        list_objs = '[]'
        with open('Square.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), list_objs)
        os.remove('Square.json')

    def test_no_arguments(self):
        """Test without arguments."""
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_too_many_arguments(self):
        """Test with too many arguments."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])


class TestBaseFromJsonString(unittest.TestCase):
    """
    This class test the class Base about the function 'from_json_string()
    """

    def test_from_json_string_rectangle(self):
        """Tests the method with a Rectangle instance."""
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_empty_rectangle(self):
        """Test with an empty string as argument."""
        list_output = Rectangle.from_json_string("")
        self.assertEqual(list_output, [])
        self.assertEqual(type(list_output), list)

    def test_from_json_string_none_rectangle(self):
        """Test with None as argument."""
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])
        self.assertEqual(type(list_output), list)

    def test_from_json_string_square(self):
        """Tests the method with a Square instance."""
        list_input = [{'id': 89, 'size': 10},
                      {'id': 7, 'size': 7}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_empty_square(self):
        """Test with an empty string as argument."""
        list_output = Square.from_json_string("")
        self.assertEqual(list_output, [])
        self.assertEqual(type(list_output), list)

    def test_from_json_string_none_square(self):
        """Test with None as argument."""
        list_output = Square.from_json_string(None)
        self.assertEqual(list_output, [])
        self.assertEqual(type(list_output), list)

    def test_from_json_string_empty_list(self):
        """Test with an empty list as arguement."""
        self.assertEqual([], Square.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        """Test without arguments."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_too_many_args(self):
        """Test with too many arguments."""
        with self.assertRaises(TypeError):
            Base.from_json_string("", 1)


class TestBaseCreate(unittest.TestCase):
    """Class that tests the Base method 'create'."""
    def test_create_rectangle(self):
        """Test creating a rectangle."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))

    def test_new_rectangle_is(self):
        """Tests if r1 is r2."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_new_rectangle_equal(self):
        """Tests if r1 == r2."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """Test creating a square."""
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))

    def test_new_square_is(self):
        """Tests if s1 is s2."""
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_new_square_equal(self):
        """Tests if s1 == s2."""
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestLoadFromFile(unittest.TestCase):
    """Class that tests the Base method 'load_from_file'."""
    def test_no_file(self):
        """Tests when the file doens't exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        output = Square.load_from_file()
        self.assertEqual(output, [])

    def test_load_from_file_rectangle(self):
        """Test with a Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        output = Rectangle.load_from_file()
        self.assertEqual(len(output), 2)
        self.assertEqual(type(output), list)
        self.assertEqual(type(output[0]), Rectangle)
        self.assertEqual(type(output[1]), Rectangle)
        self.assertEqual(output[0].to_dictionary(),
                         r1.to_dictionary())
        self.assertEqual(output[1].to_dictionary(),
                         r2.to_dictionary())

    def test_load_from_file_square(self):
        """Test with a Square instances."""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        output = Square.load_from_file()
        self.assertEqual(len(output), 2)
        self.assertEqual(type(output), list)
        self.assertEqual(type(output[0]), Square)
        self.assertEqual(type(output[1]), Square)
        self.assertEqual(output[0].to_dictionary(),
                         s1.to_dictionary())
        self.assertEqual(output[1].to_dictionary(),
                         s2.to_dictionary())


if __name__ == '__main__':
    unittest.main()
