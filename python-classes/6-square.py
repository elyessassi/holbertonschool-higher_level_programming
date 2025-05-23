#!/usr/bin/python3
"""
a class Square that defines a square size
"""


class Square:

    """
    a class Square that defines a square size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        the user defines the size and position
        the program checks if size is an int and equal or supperior to 0
        and checks if position is a tuple with 2 positive integers
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (not isinstance(position, tuple) or not isinstance(position[0], int)
           or len(position) != 2
           or not isinstance(position[1], int)
           or position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """
        getter function for position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter function for position
        """
        if (not isinstance(value, tuple) or not isinstance(value[0], int)
           or len(value) != 2
           or not isinstance(value[1], int) or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
