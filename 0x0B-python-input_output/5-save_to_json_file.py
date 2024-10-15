#!/usr/bin/python3
"""
This module contains a function that writes an object to a text file using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to write to the file.
        filename (str): The path to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
