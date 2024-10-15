#!/usr/bin/python3
"""
This module contains a function that returns an object from a JSON string.
"""


import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string.

    Returns:
        object: The corresponding Python object.
    """
    return json.loads(my_str)
