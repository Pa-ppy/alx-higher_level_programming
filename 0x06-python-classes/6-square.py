#!/usr/bin/python3
"""
This module defines a class square with size and position attributes.
"""

class Square:
    """
    A class to represent a square.

    Attributes:
        __size: size of the square (private).
        __position: position of the square (private).
    """

    def __init__(self, size=0, position=(0,0)):
        """
        Initializes the square with a given size and position.

        Args:
            size: The size of the square (default is 0).
            position: The position of the square (default is (0,0)).

    Raises:
        TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
        ValueError: If size is less than 0.
    """
    self.size = size
    self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
        value: The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value: A tuple of 2 positive integers.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            The current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#', considering position.
        If size is 0, prints an empty list.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
