#!/usr/bin/python3
""""
module that has rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """ "
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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """a method that returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """a mathod to display the rectangle"""
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print(self.width * "#")

    def __str__(self):
        """instance method that retuns the attrinutes of the Object"""
        str1 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        return str1 + f" - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """instance method that updates attributes using arguments """
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            if (kwargs.get('id') is not None):
                self.id = kwargs.get('id')
            if (kwargs.get('width') is not None):
                self.width = kwargs.get('width')
            if (kwargs.get('height') is not None):
                self.height = kwargs.get('height')
            if (kwargs.get('x') is not None):
                self.x = kwargs.get('x')
            if (kwargs.get('y') is not None):
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """dictionnary method for rectangle"""
        dic = {"x": self.x, "y": self.y, "id": self.id}
        dic['height'] = self.height
        dic["width"] = self.width
        return dic
