#!/usr/bin/python3
""" a function that returns the dictionary description with
 simple data structure (list, dictionary, string, integer and boolean) for
   JSON serialization of an object """

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def class_to_json(obj):
    """ the function """
    return (obj.__dict__)
