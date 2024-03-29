#!/usr/bin/python3
""""
defining a class rectangle

"""


class Rectangle:
    """
    defining a class rectangle with width and height instance attributes

    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
    """
    getter function for width

    """
    @property
    def width(self):
        return self.__width
    """
    setter function for width

    """
    @width.setter
    def width(self, value):
        if isinstance(value, int) == 0:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """
    getter function for height

    """
    @property
    def height(self):
        return self.__height
    """
    setter function for height

    """
    @height.setter
    def height(self, value):
        if isinstance(value, int) == 0:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
