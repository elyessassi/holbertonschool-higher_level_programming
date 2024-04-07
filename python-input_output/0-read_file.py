#!/usr/bin/python3
""" function that prints a file """
def read_file(filename=""):
    """ print the content of a file """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
