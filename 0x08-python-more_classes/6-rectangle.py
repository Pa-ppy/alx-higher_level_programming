#!/usr/bin/python3
"""
This module defines a Rectangle class that includes methods for computing area, perimeter, displaying the rectangle, recreating the object, and handling instance counting.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes:
        Width (int): The width of the rectangle.
        Height (int): The height of the rectangle.
        Number_of_instances (int): Counts the number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with width and height.
        Increments the number_of_instances class attribute.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            TypeError: If width is not an integer.
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

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        If the width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the character '#'.
        If the width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation that can recreate the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when the rectangle is deleted.
        Decrements the number_of_instances class attribute.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
