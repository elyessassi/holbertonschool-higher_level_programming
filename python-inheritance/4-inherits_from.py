#!/usr/bin/python3
"""
Write a function that returns True if the object is
an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Write a function that returns True if the object
    is an instance of a class
    that inherited (directly or indirectly
    from the specified class ; otherwise False.
    """
    return (issubclass(obj.__class__, a_class) and not
            (obj.__class__ == a_class))
