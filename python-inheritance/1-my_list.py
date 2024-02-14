#!/usr/bin/python3
"""
module that has a class that inherits from list class
"""


class MyList(list):
    """
    a class that inherits from list class
    """
    def print_sorted(self):
        """"
        print the list sorted
        """
        print(sorted(self, reverse=False))
