#!/usr/bin/python3
"""
This module defines a class 'Square' that inherits through 'Rectangle'.
The class validates the size and includes a method for calculating the area.
"""


class BaseGeometry:
    """Base class for geometry objects."""
    
    def integer_validator(self, name, value):
        """
        Validates that the given value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Square(Rectangle):
    """
    A class used to represent a Square, which inherits through Rectangle.
    
    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes the square with size.
        area(self): Calculates the area of the square.
    """

    def __init__(self, size):
        """
        Initializes the Square instance with size.

        Args:
            size (int): The size of the square, validated by integer_validator.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
