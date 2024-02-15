#!/usr/bin/python3
""""
module that has rectangle class
"""
from models.base import Base
""""
rectangle class
Args:
    width: width of rectangle
    height: height of rectangle
    x
    y
"""


class Rectangle(Base):
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, x):
            self.__width = x

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, x):
            self.height = x

        @property
        def x(self):
            return self.__x

        @x.setter
        def width(self, x):
            self.__x = x

        @property
        def y(self):
            return self.__y

        @y.setter
        def width(self, x):
            self.__y = x
