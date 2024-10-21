#!/usr/bin/python3
"""
Unit tests for the Square class.
"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_square_init(self):
        """Test instantiation of Square."""
        s1 = Square(10, 1, 2, 3)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 3)

    def test_invalid_size_type(self):
        """Test invalid size type."""
        with self.assertRaises(TypeError):
            Square("10")

    def test_invalid_size_value(self):
        """Test invalid size value."""
        with self.assertRaises(ValueError):
            Square(-10)

    def test_update_args(self):
        """Test update method with *args."""
        s1 = Square(10, 1, 2, 3)
        s1.update(100, 20, 5, 6)
        self.assertEqual(s1.id, 100)
        self.assertEqual(s1.size, 20)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 6)

    def test_update_kwargs(self):
        """Test update method with **kwargs."""
        s1 = Square(10, 1, 2, 3)
        s1.update(id=200, size=30, x=5, y=3)
        self.assertEqual(s1.id, 200)
        self.assertEqual(s1.size, 30)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 3)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s1 = Square(10, 1, 2, 3)
        s1_dict = s1.to_dictionary()
        expected_dict = {'id': 3, 'size': 10, 'x': 1, 'y': 2}
        self.assertEqual(s1_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()
