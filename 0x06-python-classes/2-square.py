#!/usr/bin/python3
"""
This module defines a class Square with size validation
"""

class Square:
    """
    A class to represent a square.

    Attributes:
        __size: size of the square (private)
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size

        Args:
            size: The size of the square (default is 0).

        Raises:
        TypeError: If size is not an integer
        ValueError: If  size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
