#!/usr/bin/python3
""""
defining a class rectangle
"""


class Rectangle:
    """
    defining a class rectangle with width and height instance attributes
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) == 0:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) == 0:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
