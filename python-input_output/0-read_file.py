#!/usr/bin/python3
""" function that prints a file """
def read_file(filename="", encoding="UTF8"):
    """ print the content of a file """
    with open(filename) as f:
        print(f.read(), end="")
