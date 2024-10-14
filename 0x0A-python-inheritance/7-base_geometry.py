#!/usr/bin/python3
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
        Raises TypeError if value is not an integer and ValueError if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("f{name} must be an integer")
        if value <= 0:
            raise ValueError("f{name} must be greater than 0")
