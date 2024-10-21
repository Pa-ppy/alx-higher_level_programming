#!/usr/bin/python3
"""
This module provides a Square class that inherits from Rectangle.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle and handles size attribute.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square with size, x, y, and id."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square (equivalent to width)."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square and applies the same value to width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overrides the __str__ method to return [Square] (<id>) <x>/<y> - <size>.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Assign attributes using *args (no-keyworded) or **kwargs (keyworded)."""
        if args:
            attr_list = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attr_list):
                    setattr(self, attr_list[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
            }
