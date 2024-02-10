#!/usr/bin/python3
""""
defining a class rectangle

"""


class Rectangle:
    number_of_instances = 0
    """
    defining a class rectangle with width and height instance attributes
    number_of_instances:used to know the number of instances created

    """
    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.__height = height
        self.__width = width
        self.number_of_instances = Rectangle.number_of_instances
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
    """
    area instance attribute to get the area of a rectangle
    """
    def area(self):
        return self.__height * self.__width
    """
    perimeter instance attribute to get the perimeter of a rectangle
    """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.width):
                    print("#", end="")
                if i != (self.__height - 1):
                    print("")
            return ""

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
