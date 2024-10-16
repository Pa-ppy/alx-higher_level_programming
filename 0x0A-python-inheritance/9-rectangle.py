#!/usr/bin/python3
"""
This module defines a class 'Rectangle' that inherits from 'BaseGeometry'.
It includes methods for calculating area and representing the rectangle as a string.
"""


from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle, which inherits from BaseGeometry.
    
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes the rectangle with width and height.
        area(self): Calculates the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle, validated by integer_validator.
            height (int): The height of the rectangle, validated by integer_validator.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"