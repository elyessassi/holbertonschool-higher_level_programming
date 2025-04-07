#!/usr/bin/python3
""" Student class """


class Student:
    """ The class """

    def __init__(self, first_name, last_name, age):
        """ Constructor method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns all attributes with values """
        if (attrs is None):
            return (self.__dict__)
        new_dict = {}
        for i in attrs:
            for j in self.__dict__:
                if (i == j):
                    new_dict[j] = self.__dict__[i]
        return (new_dict)

    def reload_from_json(self, json):
        """ reloading attributes form json """
        self.__dict__ = json
