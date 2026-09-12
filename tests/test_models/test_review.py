#!/usr/bin/python3
"""Unit tests for Review class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review."""

    def test_instance(self):
        """Test Review instance."""
        r = Review()
        self.assertIsInstance(r, Review)

    def test_inherits_basemodel(self):
        """Test Review inherits from BaseModel."""
        r = Review()
        self.assertIsInstance(r, BaseModel)

    def test_place_id(self):
        """Test place_id attribute."""
        r = Review()
        self.assertEqual(r.place_id, "")

    def test_user_id(self):
        """Test user_id attribute."""
        r = Review()
        self.assertEqual(r.user_id, "")

    def test_text(self):
        """Test text attribute."""
        r = Review()
        self.assertEqual(r.text, "")


if __name__ == "__main__":
    unittest.main()
