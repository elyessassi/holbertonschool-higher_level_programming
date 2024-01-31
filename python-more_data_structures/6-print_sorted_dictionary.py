#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sd = dict(sorted(a_dictionary.items()))
    for i, j in sd.items():
        print(f"{i}: {j}")
