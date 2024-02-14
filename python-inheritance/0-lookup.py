#!/usr/bin/python3
"""
a module that provides
a function that returns the list of attributes and methods of an object
"""


def lookup(obj):
    """
    a function that returns the list of attributes and methods of an object
    """
    return dir(obj)
