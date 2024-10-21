#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_rectangle_init(self):
        """Test instantiation of Rectangle."""
        r1 = Rectangle(10, 5, 0, 0, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_invalid_width_type(self):
        """Test invalid width type."""
        with self.assertRaises(TypeError):
            Rectangle("10", 5)

    def test_invalid_height_value(self):
        """Test invalid height value."""
        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_area(self):
        """Test area method."""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.area(), 50)

    def test_update_args(self):
        """Test update method with *args."""
        r1 = Rectangle(10, 5, 0, 0, 1)
        r1.update(100, 20, 30, 1, 2)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 30)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)

    def test_update_kwargs(self):
        """Test update method with **kwargs."""
        r1 = Rectangle(10, 5, 0, 0, 1)
        r1.update(id=200, width=15, height=25, x=5, y=3)
        self.assertEqual(r1.id, 200)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 25)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 3)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r1 = Rectangle(10, 5, 0, 0, 1)
        r1_dict = r1.to_dictionary()
        expected_dict = {'id': 1, 'width': 10, 'height': 5, 'x': 0, 'y': 0}
        self.assertEqual(r1_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()
