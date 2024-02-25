#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constractor that calls the contarctor of parent class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """instance method that returns the attrinutes of the Object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter method for size"""
        return self.width

    @size.setter
    def size(self, size):
        """setter method for size"""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        self.height = size
        self.width = size

    def update(self, *args, **kwargs):
        """method that updates the object using args and kwargs"""
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            if (kwargs.get('id') is not None):
                self.id = kwargs.get('id')
            if (kwargs.get('size') is not None):
                self.width = kwargs.get('size')
                self.height = kwargs.get('size')
            if (kwargs.get('x') is not None):
                self.x = kwargs.get('x')
            if (kwargs.get('y') is not None):
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """dictionnary method for square"""
        dic = {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
        return dic
