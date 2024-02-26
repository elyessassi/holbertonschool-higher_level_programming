#!/usr/bin/python3
"""
script that manages id attributes
"""

import json


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
        """save a list of obj to a file (Json format) """
        if list_objs is None:
            list_objs = []
        else:
            for i in range(len(list_objs)):
                list_objs[i] = list_objs[i].to_dictionary()
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """convert a json string to list"""
        if (json_string is None) or (len(json_string) == 0):
            return []
        else:
            return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """create an instance with dictionnary"""
        i = cls(1, 2)
        i.update(**dictionary)
        return i
