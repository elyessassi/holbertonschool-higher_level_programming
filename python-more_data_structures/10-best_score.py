#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    s = max(a_dictionary.values())
    list = [x for x, y in a_dictionary.items() if y == s]
    return (list[0])
