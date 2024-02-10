#!/usr/bin/python3
""""
defining a class rectangle

"""


class Rectangle:
    """
    class attribute that holds the number of instances
    """
    number_of_instances = 0
    print_symbol = "#"

    """
    defining a class rectangle with width and height instance attributes

    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

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
                    print(self.print_symbol, end="")
                if i != (self.__height - 1):
                    print("")
            return ""

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_1.area() < rect_2.area():
                return rect_2
            else:
                return rect_1

    @classmethod
    def square(cls, size=0):
        """
        return a rectangle instance that has size as input
        Args:
            size (int): the size of the square
        Returns:
            (Rectangle): rectangle instance
        """
        return cls(size, size)
