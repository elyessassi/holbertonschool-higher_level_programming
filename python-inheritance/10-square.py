#!/usr/bin/python3
""" Square Class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        """ Constructor method """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns the area """
        return self.__size * self.__size
