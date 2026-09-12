#!/usr/bin/python3
"""Unit tests for Place class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place."""

    def test_instance(self):
        """Test Place instance."""
        p = Place()
        self.assertIsInstance(p, Place)

    def test_inherits_basemodel(self):
        """Test Place inherits from BaseModel."""
        p = Place()
        self.assertIsInstance(p, BaseModel)

    def test_city_id(self):
        """Test city_id attribute."""
        p = Place()
        self.assertEqual(p.city_id, "")

    def test_user_id(self):
        """Test user_id attribute."""
        p = Place()
        self.assertEqual(p.user_id, "")

    def test_name(self):
        """Test name attribute."""
        p = Place()
        self.assertEqual(p.name, "")

    def test_number_rooms(self):
        """Test number_rooms attribute."""
        p = Place()
        self.assertEqual(p.number_rooms, 0)

    def test_latitude(self):
        """Test latitude attribute."""
        p = Place()
        self.assertEqual(p.latitude, 0.0)


if __name__ == "__main__":
    unittest.main()
