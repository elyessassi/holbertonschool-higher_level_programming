#!/usr/bin/python3
"""a function that returns the JSON representation"""

import json


def to_json_string(my_obj):
    """ to jsob string"""
    return json.dumps(my_obj)
