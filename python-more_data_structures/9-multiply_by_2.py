#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = {}
    for key in a_dictionary:
        d[key] = a_dictionary.get(key, 0) * 2
    return d
