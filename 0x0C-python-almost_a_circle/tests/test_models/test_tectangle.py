#!/usr/bin/python3
"""
Unit tests for the Rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def test_init(self):
        """Test the initialization of Rectangle instances."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

        r2 = Rectangle(3, 5, 1, 2, 12)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        self.assertEqual(r2.id, 12)

    def test_area(self):
        """Test the area method."""
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)

    def test_str(self):
        """Test the __str__ method."""
        r1 = Rectangle(4, 6, 2, 1, 15)
        self.assertEqual(str(r1), "[Rectangle] (15) 2/1 - 4/6")

    def test_display(self):
        """Test the display method."""
        r1 = Rectangle(3, 2)
        output = "###\n###\n"
        with self.assertLogs() as log:
            r1.display()
        self.assertIn(output, log.output)

    def test_update_args(self):
        """Test the update method with *args."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_invalid_type(self):
        """Test invalid types for width, height, x, and y."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

        with self.assertRaises(TypeError):
            Rectangle(10, "2")

        with self.assertRaises(TypeError):
            Rectangle(10, 2, "3", 0)

        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "3")

    def test_invalid_value(self):
        """Test invalid values for width, height, x, and y."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

        with self.assertRaises(ValueError):
            Rectangle(10, -2)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3, 0)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -3)

if __name__ == '__main__':
    unittest.main()
