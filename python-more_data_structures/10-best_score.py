#!/usr/bin/python3
def best_score(a_dictionary):
    return (max(a_dictionary, default=None, key=a_dictionary.get))
