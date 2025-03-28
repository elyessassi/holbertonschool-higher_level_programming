#!/usr/bin/python3

"""
a function that prints a square with the character #
"""


def print_square(size):
    """ a function that prints a square """

    if (not isinstance(size, (int, float))):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(int(size)):
        print("#" * int(size))


if (__name__ == "__main__"):
    import doctest
    doctest.testfile("tests/4-print_square.txt")
