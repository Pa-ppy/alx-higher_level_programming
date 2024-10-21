#!/usr/bin/python3
"""
Unit tests for the Base class.
"""


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Test to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """Test to_json_string with a valid list of dictionaries."""
        list_dicts = [{"id": 1, "width": 3}, {"id": 2, "width": 5}]
        json_string = Base.to_json_string(list_dicts)
        self.assertTrue(isinstance(json_string, str))

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string(self):
        """Test from_json_string with a valid JSON string."""
        json_str = '[{"id": 1, "width": 3}, {"id": 2, "width": 5}]'
        list_dicts = Base.from_json_string(json_str)
        self.assertTrue(isinstance(list_dicts, list))
        self.assertEqual(len(list_dicts), 2)

    def test_save_to_file_none(self):
        """Test save_to_file with None."""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")
        os.remove("Base.json")

    def test_save_to_file(self):
        """Test save_to_file with a list of objects."""
        r1 = Rectangle(5, 10, 1, 2, 10)
        r2 = Rectangle(3, 6, 0, 0, 20)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertTrue(len(content) > 0)
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Test load_from_file when no file exists."""
        list_objs = Rectangle.load_from_file()
        self.assertEqual(list_objs, [])

    def test_load_from_file(self):
        """Test load_from_file with a valid file."""
        r1 = Rectangle(5, 10, 1, 2, 10)
        r2 = Rectangle(3, 6, 0, 0, 20)
        Rectangle.save_to_file([r1, r2])
        list_objs = Rectangle.load_from_file()
        self.assertEqual(len(list_objs), 2)
        os.remove("Rectangle.json")

    def test_create(self):
        """Test create method."""
        r1 = Rectangle(3, 5, 1, 2, 100)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r1.__str__(), r2.__str__())

if __name__ == "__main__":
    unittest.main()
