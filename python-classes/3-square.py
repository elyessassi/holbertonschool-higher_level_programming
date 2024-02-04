#!/usr/bin/python3
"""
a class Square that defines a square size
"""


class Square:

    """
    a class Square that defines a square size
    """

    def __init__(self, size=0):
        """
        the user defines the size
        the program checks if size is an int and equal or supperior to 0
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        instance to get the current square area
        """
        return self.__size ** 2
