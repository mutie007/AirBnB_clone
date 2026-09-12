#!/usr/bin/python3
"""Unit tests for Amenity class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity."""

    def test_instance(self):
        """Test Amenity instance."""
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_inherits_basemodel(self):
        """Test Amenity inherits from BaseModel."""
        a = Amenity()
        self.assertIsInstance(a, BaseModel)

    def test_name(self):
        """Test name attribute."""
        a = Amenity()
        self.assertEqual(a.name, "")


if __name__ == "__main__":
    unittest.main()
