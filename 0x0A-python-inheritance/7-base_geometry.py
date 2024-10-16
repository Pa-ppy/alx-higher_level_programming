#!/usr/bin/python3
"""
This module defines a class 'BaseGeometry' with two methods:
area which raises an Exception because it is not implemented.
integer_validator which validates that a value is an integer
and greater than 0.
"""


class BaseGeometry:
    """
    Class BaseGeometry with area method and integer validator
    """

    def area(self):
        """
        Raises an exception with message,'area is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is an integer and greater than zero

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to be validated.

        Raises:
            TypeError: if value is not an integer
            ValueError: if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("f{name} must be an integer")
        if value <= 0:
            raise ValueError("f{name} must be greater than 0")
