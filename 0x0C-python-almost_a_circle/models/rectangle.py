#!/usr/bin/python3
"""
This module provides a Rectangle class that inherits from Base.
It manages width, height, x, and y attributes with validation.
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base and handles attributes width, height, x, y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle class with width, height, x, y, and id.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Prints the rectangle using the character # without handling x and y.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Overrides the str method to return a formatted string
        representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """
        Assign attributes using *args (no-keyworded) or **kwargs (keyworded).
        """
        if args:
            attr_list = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attr_list):
                    setattr(self, attr_list[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.
        """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
