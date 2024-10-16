#!/usr/bin/python3
"""
This module defines a function that checks if an object is an
instance of or if the object is an instance of a class that inherited
through the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance, or an instance that
    inherited by the specified class
    Otherwise returns False.
    """
    return isinstance(obj, a_class)
