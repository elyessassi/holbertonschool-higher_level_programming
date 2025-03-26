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

    @property
    def size(self):
        """
        getter function that gets the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter function that sets the size
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        method to get the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if (self.__size == 0):
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
