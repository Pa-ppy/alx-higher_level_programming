#!/usr/bin/python3
"""
This module defines a function is_same_class that checks if
an object is exactly an instance
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of specified class
    Otherwise return False
    """
    return type(obj) is a_class
