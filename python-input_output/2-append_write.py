#!/usr/bin/python3
""" a function that appends a string """


def append_write(filename="", text=""):
    """append a string"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
