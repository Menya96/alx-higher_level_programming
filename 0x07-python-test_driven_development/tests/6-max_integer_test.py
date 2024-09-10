#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest test cases for function max_integer"""

    def test_empty_list(self):
        """Tests empty list"""
        self.assertEqual(max_integer([]), None)

    def test_positive_ints(self):
        """Tests a list with positive integers"""
        self.assertEqual(max_integer([2, 5, 8]), 8)

    def test_negative_ints(self):
        """Tests a list with negative integers"""
        self.assertEqual(max_integer([-2, -5, -8]), -2)

    def test_mixed_ints(self):
        """Tests a list of positive and negative ints"""
        self.assertEqual(max_integer([4, -3, 1, -8, 5]), 5)

    def test_positive_floats(self):
        """Tests list with positive floats"""
        self.assertEqual(max_integer([5.6, 7.4, 1.9]), 7.4)

    def test_negative_floats(self):
        """Tests list with negative floats"""
        self.assertEqual(max_integer([-5.6, -7.4, -1.9]), -1.9)

    def test_mixed_floats(self):
        """Tests a list of positive and negative floats"""
        self.assertEqual(max_integer([4.3, -3, 1.9, -8.8, 5.5]), 5.5)

    def test_positive_ints_and_floats(self):
        """Tests a list of positive ints and floats"""
        self.assertEqual(max_integer([2.4, 7, 9.8, 9]), 9.8)

    def test_negative_ints_and_floats(self):
        """Tests a list of negative ints and floats"""
        self.assertEqual(max_integer([-2, -7, -9.8, -9]), -2)

    def test_mixed(self):
        """Tests a list of mixed positive and negative integers and floats"""
        self.assertEqual(max_integer([8, -7.3, 4, -5.7, -1, 2.2]), 8)

    def test_same_int(self):
        """Test a list with similar integer"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_same_float(self):
        """Test a list with similar float"""
        self.assertEqual(max_integer([-3, -3, -3, -3]), -3)

    def test_string(self):
        """Tests the string passed"""
        self.assertEqual(max_integer("basketball"), "t")

    def test_one_item_list(self):
        """Test a list containing only one item"""
        self.assertEqual(max_integer([2]), 2)

    def test_list_strings(self):
        """Tests a list full of strings"""
        self.assertEqual(max_integer(["toy", "uber", "engine"]), "uber")


if __name__ == "__main__":
    unittest.main()
