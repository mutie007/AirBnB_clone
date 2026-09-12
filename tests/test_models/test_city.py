#!/usr/bin/python3
"""Unit tests for City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City."""

    def test_instance(self):
        """Test City instance."""
        c = City()
        self.assertIsInstance(c, City)

    def test_inherits_basemodel(self):
        """Test City inherits from BaseModel."""
        c = City()
        self.assertIsInstance(c, BaseModel)

    def test_state_id(self):
        """Test state_id attribute."""
        c = City()
        self.assertEqual(c.state_id, "")

    def test_name(self):
        """Test name attribute."""
        c = City()
        self.assertEqual(c.name, "")


if __name__ == "__main__":
    unittest.main()
