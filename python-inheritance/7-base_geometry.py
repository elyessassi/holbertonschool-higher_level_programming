#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """ class BaseGeometry with method area that raises an exception"""
    def area(self):
        """ raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates the value given """
        if (not isinstance(value, int)):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
