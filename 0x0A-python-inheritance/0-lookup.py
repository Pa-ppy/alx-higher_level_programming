#!/usr/bin/python3
"""
This module defines a function lookup that returns the list
of available attributes
"""
def lookup(obj):
    """
    Returns the list of the available attributes/methods of an object
    """
    return dir(obj)
