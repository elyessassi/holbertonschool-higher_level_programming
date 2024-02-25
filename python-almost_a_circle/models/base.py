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

    def to_json_string(list_dictionaries):
        """method that returns JSON format of list_dictionnaries"""
        if list_dictionaries is None or list_dictionaries[0] is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
