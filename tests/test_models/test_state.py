#!/usr/bin/python3
"""Unit tests for State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State."""

    def test_instance(self):
        """Test State instance."""
        s = State()
        self.assertIsInstance(s, State)

    def test_inherits_basemodel(self):
        """Test State inherits from BaseModel."""
        s = State()
        self.assertIsInstance(s, BaseModel)

    def test_name(self):
        """Test name attribute."""
        s = State()
        self.assertEqual(s.name, "")


if __name__ == "__main__":
    unittest.main()
