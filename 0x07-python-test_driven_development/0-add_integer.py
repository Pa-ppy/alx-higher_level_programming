#!/usr/bin/python3
"""
This module defines a function that adds two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer

    Args:
        a (int, float): First number.
        b (int, float): Second number (default is 98).

    Returns:
        int: The result of the addition.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance("b must be an integer")

    return int(a) + int(b)
