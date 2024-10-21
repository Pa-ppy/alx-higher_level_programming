#!/usr/bin/python3
"""
Unit tests for the Base class
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def test_no_id(self):
        """Test when no id is passed."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_with_id(self):
        """Test when an id is passed."""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_mixed_id(self):
        """Test with a mix of None and provided id."""
        b4 = Base()
        b5 = Base(25)
        b6 = Base()
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 25)
        self.assertEqual(b6.id, 4)

if __name__ == '__main__':
    unittest.main()
