#!/usr/bin/python3
"""
This modules defines a class Square with private size attribute.
"""

class Square:
    """
    A class to represent a square.

    Attributes:
        __size: size of the square (private).
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.


        Args:
            size: The size of the square
        """
        self.__size = size
