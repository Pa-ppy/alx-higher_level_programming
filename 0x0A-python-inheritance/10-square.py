#!/usr/bin/python3
"""
This module defines a class 'Square' that inherits from 'Rectangle'.
The class validates the size and includes a method for calculating the area.
"""


from 9-rectangle import Rectangle


class Square(Rectangle):
    """
    A class used to represent a Square, which inherits from Rectangle.
    
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
