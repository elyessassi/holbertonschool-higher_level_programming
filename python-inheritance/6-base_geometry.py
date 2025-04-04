#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """ class BaseGeometry with method area that raises an exception"""
    def area(self):
        """ raises an exception """
        raise Exception("area() is not implemented")
