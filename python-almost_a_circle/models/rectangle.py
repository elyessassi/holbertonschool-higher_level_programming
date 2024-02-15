#!/usr/bin/python3
""""
module that has rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """"
    rectangle class
    Args:
        width: width of rectangle
        height: height of rectangle
        x
        y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constactor that gets width height x and y"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """getter method for width"""
            return self.__width

        @width.setter
        def width(self, x):
            """setter method for width"""
            self.__width = x

        @property
        def height(self):
            """getter method for height"""
            return self.__height

        @height.setter
        def height(self, x):
            """setter method for height"""
            self.height = x

        @property
        def x(self):
            """getter method for x"""
            return self.__x

        @x.setter
        def width(self, x):
            """setter method for x"""
            self.__x = x

        @property
        def y(self):
            """getter method for y"""
            return self.__y

        @y.setter
        def width(self, x):
            """setter method for y"""
            self.__y = x
