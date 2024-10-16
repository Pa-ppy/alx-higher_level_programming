#!/usr/bin/python3
"""
This modules defines a function that checks if an object is an instance
of a class that inherited directly or indirectly by the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited by the specified class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
