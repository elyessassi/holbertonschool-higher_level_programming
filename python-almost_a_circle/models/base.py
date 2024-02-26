#!/usr/bin/python3
"""
script that manages id attributes
"""

import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """method that returns JSON format of list_dictionnaries"""
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method """
        if list_objs is None:
            list_objs = []
        else:
            for i in range(len(list_objs)):
                list_objs[i] = list_objs[i].to_dictionary()
        with open(f"{cls.__name__}.json", "w") as f:
            json.dump(list_objs, f)
