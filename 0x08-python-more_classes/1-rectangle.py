#!/usr/bin/python3
"""
This module defines a Rectangle class.
The class contains private instance attributes for width and height.
"""


class Rectangle:
    """
    A class that is used to represent a Rectangle.

    Attributes:
        width: The width of the rectangle.
        height: The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
