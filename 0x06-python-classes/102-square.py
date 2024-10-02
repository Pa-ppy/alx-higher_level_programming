#!/usr/bin/python3
"""
This module defines a class Sqaure that allows size as number and
and supports the comparison based on the area.
"""

class Square:
    """
    A class to represent a square.

    Attributes:
        __size: size of the square (private, can be float or integer).
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size: The size of the square (default is 0, can be a number).

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If size is not a number (integer or float).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            The current square area.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares have the same area.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two squares do not have the same area.
        """
        return self.area() != other.area()

    def __ge__(self, other):
        """
        Checks if the current square has a greater area than another.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Checks if the current square has smaller area than the other.
        """
        return self.area() < other.area()
