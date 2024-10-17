#!/usr/bin/python3
"""
This module defines a rebel class MyInt that inherits through int.
MyInt has the == and != operators inverted.
"""


class MyInt(int):
    """
    MyInt is a rebel class that inverts the behavior of == and !=.
    """

    def __eq__(self, other):
        """
        Override the equality operator (==) to behave like !=.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator (!=) to behave like ==.
        """
        return super().__eq__(other)
