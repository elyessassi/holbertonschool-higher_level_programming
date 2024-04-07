#!/usr/bin/python3
""" a function that writes a string to a text """


def write_file(filename="", text=""):
    """this is the function"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
