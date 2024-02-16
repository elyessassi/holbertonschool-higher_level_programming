#!/usr/bin/python3
"""unit testing Base class"""

import unittest
import models.base
from models.base import Base


class Testbase(unittest.TestCase):
    """class for unit tests"""

    def test_case1(self):
        """case 1"""
        b1 = Base(10)
        b2 = Base(17)
        b3 = Base()
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 17)
        self.assertEqual(b3.id, 1)

    def test_case2(self):
        """case 2"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)


if __name__ == "__main__":
    unittest.main()
