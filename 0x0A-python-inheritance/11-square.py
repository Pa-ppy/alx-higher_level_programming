#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle
and provides a string representation of the square.
"""


class BaseGeometry:
    """
    BaseGeometry class with validation methods.
    """

    def area(self):
        """
        Raises an Exception for area not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as a positive integer.

        Args:
            name (str): The name of the variable.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class that defines a rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


class Square(Rectangle):
    """
    Square class that represents a square shape.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: The square description in the format [Square] <size>/<size>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
