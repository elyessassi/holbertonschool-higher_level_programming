#!/usr/bin/python3
""" class Student that defines a student """


class Student:
    """ The class """

    def __init__(self, first_name, last_name, age):
        """ Constructor method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns all attributes with values """
        return (self.__dict__)
