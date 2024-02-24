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
