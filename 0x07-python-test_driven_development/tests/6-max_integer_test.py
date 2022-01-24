#!/usr/bin/python3
"""
Add Unittest for the function max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    The class TestMaxInteger tests to find the max integer.
    """
    def test_max_integers(self):
        """
        Tests about:
            - integers: positive and negative
            - float: positive and negative
            - characters
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([4, -2, 8, 12, -20]), 12)

        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([10.5, 5.1]), 10.5)
        self.assertEqual(max_integer([1.99, -6.77]), 1.99)
        self.assertEqual(max_integer([1, 3.4, 30, 99.99, 5]), 99.99)

        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([0]), 0)

        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(['e', 'l', 'o', 'd', 'i', 'e']), 'o')

        self.assertEqual(max_integer(["Hello", "World"]), "World")
        self.assertEqual(max_integer(["holberton", "school", "laval"]), "school")

    def test_exceptions(self):
        """
        Tests about exceptions:
            - Empty
            - None
            - one integer
            - Multiple type (string + integer)
        """
        self.assertIsNone(max_integer([]))
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer(5)
        with self.assertRaises(TypeError):
            max_integer(["Holberton", 23, "School", 53])


if __name__ == '__main__':
    unittest.main()
