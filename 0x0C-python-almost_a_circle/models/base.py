#!/usr/bin/python3
"""
This module provides a Base class to manage the id attribute in all future classes.
The goal is to centralize the logic and avoid redundancy.
"""


class Base:
    """
    Base class for managing 'id' attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base class with an optional id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
