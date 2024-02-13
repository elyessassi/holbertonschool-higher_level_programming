#!/usr/bin/python3
"""
script that manages id attributes
"""


class Base:
    """
    a class that manages id attributes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
