#!/usr/bin/python3
"""Unit tests for User class."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User."""

    def test_instance(self):
        """Test User instance."""
        u = User()
        self.assertIsInstance(u, User)

    def test_inherits_basemodel(self):
        """Test User inherits from BaseModel."""
        u = User()
        self.assertIsInstance(u, BaseModel)

    def test_email(self):
        """Test email attribute."""
        u = User()
        self.assertEqual(u.email, "")

    def test_password(self):
        """Test password attribute."""
        u = User()
        self.assertEqual(u.password, "")

    def test_first_name(self):
        """Test first_name attribute."""
        u = User()
        self.assertEqual(u.first_name, "")

    def test_last_name(self):
        """Test last_name attribute."""
        u = User()
        self.assertEqual(u.last_name, "")


if __name__ == "__main__":
    unittest.main()
