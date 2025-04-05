#!/usr/bin/python3
""" Rectangle class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Retangle class that gets height and width"""
    def __init__(self, width, height):
        """ Constructor method """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ method that returns the area if the rectangle """
        return (self.__height * self.__width)

    def __str__(self):
        """ string format """
        return (f"[Rectangle] {self.__width}/{self.__height}")
