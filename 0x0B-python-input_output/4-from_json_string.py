#!/usr/bin/python3
"""Module 4-from_json_string
returns an object represented by a JSON string
"""


import json


def from_json_string(my_str):
    """Returns an object
    Arg:
    my_str: JSON string
    """

    return json.loads(my_str)
