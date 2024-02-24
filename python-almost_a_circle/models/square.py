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
