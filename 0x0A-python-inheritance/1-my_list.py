#!/usr/bin/python3
"""
This module defines a class that contains a method that prints
the list sorted in ascending order
"""


class MyList(list):
    """
    Inherits list and provides a method to print sorted list
    """

    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))
