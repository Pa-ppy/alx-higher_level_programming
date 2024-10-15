#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description
with simple data structures for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: The object to serialize.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__
