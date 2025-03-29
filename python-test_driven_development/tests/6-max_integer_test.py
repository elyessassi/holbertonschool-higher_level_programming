#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class that has the text cases """

    def test_common_case(self):
        """ common case """

        x = max_integer([1, 3, 4, 2])
        self.assertEqual(x, 4)

    def test_empty_list_case(self):
        """ Case where the list is empty """

        x = max_integer([])
        self.assertIsNone(x)

    def test_max_at_the_end(self):
        """ Case where the max value is in the end """

        x = max_integer([1, 3, 2, 4])
        self.assertEqual(4, x)

    def test_max_at_the_start(self):
        """ Case where the max value is at the start """

        x = max_integer([4, 3, 2, 1])
        self.assertEqual(4, x)

    def test_two_max_values(self):
        """ Case where there are two max values """

        x = max_integer([4, 3, 4, 1])
        self.assertEqual(4, x)

    def test_one_negative_value(self):
        """ Case where there is 1 negaive value """

        x = max_integer([4, -3, 2, 1])
        self.assertEqual(4, x)

    def test_list_of_negative_values(self):
        """ Case where all the elements are negative """

        x = max_integer([-4, -3, -2, -1])
        self.assertEqual(-1, x)

    def test_one_element(self):
        """ Case where there is one element in the list """

        x = max_integer([2])
        self.assertEqual(2, x)


if (__name__ == "__main__"):
    unittest.main()
