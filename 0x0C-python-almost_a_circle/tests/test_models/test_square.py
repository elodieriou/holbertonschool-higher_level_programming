#!/usr/bin/python3
"""
Add unit test for the class Square
"""
import unittest
from models.base import Base
from models.square import Square


class TestSquareUpdateAttribute(unittest.TestCase):
    """This class test the class Square that can update the attributes"""

    def tests_update_args_attrs(self):
        """Tests to update with *args attributes"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual("[Square] (1) 0/0 - 5", str(s1))
        s1.update(10)
        self.assertEqual(s1.id, 10)
        self.assertEqual("[Square] (10) 0/0 - 5", str(s1))
        s1.update(1, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual("[Square] (1) 0/0 - 2", str(s1))
        s1.update(1, 2, 3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual("[Square] (1) 3/0 - 2", str(s1))
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s1))

    def tests_update_kwargs_attrs(self):
        """Tests to update with **kwargs attributes"""
        s1 = Square(1, 2, 3, 4)
        s1.update(x=12)
        self.assertEqual(s1.x, 12)
        self.assertEqual("[Square] (4) 12/3 - 1", str(s1))
        s1.update(size=7, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.y, 1)
        self.assertEqual("[Square] (4) 12/1 - 7", str(s1))
        s1.update(size=7, id=89, y=6)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 6)
        self.assertEqual("[Square] (89) 12/6 - 7", str(s1))

    def test_update_kwargs_skipped(self):
        """Test that **kwargs is skipped if *args exist"""
        s1 = Square(1, 2, 3, 4)
        s1.update(9, x=12)
        self.assertEqual("[Square] (9) 2/3 - 1", str(s1))

    def test_without_attrs(self):
        """Test without attributes"""
        s1 = Square(1, 2, 3, 4)
        s1.update()
        self.assertEqual("[Square] (4) 2/3 - 1", str(s1))

    def test_update_id_none(self):
        """Test a None attribute"""
        s1 = Square(1, 2, 3, 4)
        s1.update(None)
        self.assertEqual("[Square] (None) 2/3 - 1", str(s1))

    def test_update_id_zero(self):
        """Test id as zero"""
        s1 = Square(1, 2, 3, 4)
        s1.update(0)
        self.assertEqual("[Square] (0) 2/3 - 1", str(s1))

    def test_update_id_string(self):
        """Test id as a string"""
        s1 = Square(1, 2, 3, 4)
        s1.update('hello')
        self.assertEqual("[Square] (hello) 2/3 - 1", str(s1))

    def test_update_size_zero(self):
        """Test size as zero"""
        s1 = Square(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            s1.update(size=0)

    def test_update_size_string(self):
        """Test size as a string"""
        s1 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s1.update(size='hello')

    def test_update_x_negative(self):
        """Test x as a negative integer"""
        s1 = Square(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            s1.update(x=-1)

    def test_update_x_string(self):
        """Test x as a string"""
        s1 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s1.update(x='hello')

    def test_update_y_negative(self):
        """Test y as a negative integer"""
        s1 = Square(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            s1.update(y=-1)

    def test_update_y_string(self):
        """Test y as a string"""
        s1 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s1.update(y='hello')


class TestSquareToDictionary(unittest.TestCase):
    """
    This class test the class Square that returns the dictionary
    representation of a Square.
    """
    def test_dictionary_representation(self):
        """Test the dictionary representation of a Square"""
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertEqual(type(s1_dictionary), dict)

    def test_dictionary_compare(self):
        """Test to compare dictionaries"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1.__dict__, s2.__dict__)
        self.assertFalse(s1 == s2)

    def test_dictionary_add_args(self):
        """Test to add one argument"""
        s1 = Square(10, 2, 1)
        with self.assertRaises(TypeError):
            s1.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()
