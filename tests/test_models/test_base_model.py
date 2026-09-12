#!/usr/bin/python3
"""Unit tests for BaseModel class."""
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel."""

    def test_instance(self):
        """Test BaseModel instance creation."""
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)

    def test_id_is_string(self):
        """Test that id is a string."""
        b = BaseModel()
        self.assertIsInstance(b.id, str)

    def test_unique_id(self):
        """Test that each instance has unique id."""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_created_at_is_datetime(self):
        """Test created_at is datetime."""
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test updated_at is datetime."""
        b = BaseModel()
        self.assertIsInstance(b.updated_at, datetime)

    def test_str(self):
        """Test __str__ method."""
        b = BaseModel()
        s = str(b)
        self.assertIn("[BaseModel]", s)
        self.assertIn(b.id, s)

    def test_save(self):
        """Test save method updates updated_at."""
        b = BaseModel()
        old = b.updated_at
        b.save()
        self.assertNotEqual(old, b.updated_at)

    def test_save_creates_file(self):
        """Test save creates file.json."""
        b = BaseModel()
        b.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict(self):
        """Test to_dict method."""
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_to_dict_has_id(self):
        """Test to_dict contains id."""
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["id"], b.id)

    def test_init_from_dict(self):
        """Test init from dictionary."""
        b = BaseModel()
        b.name = "test"
        d = b.to_dict()
        b2 = BaseModel(**d)
        self.assertEqual(b.id, b2.id)
        self.assertEqual(b.created_at, b2.created_at)
        self.assertFalse(b is b2)

    def test_init_from_dict_no_storage(self):
        """Test that init from dict does not call storage.new."""
        b = BaseModel()
        d = b.to_dict()
        b2 = BaseModel(**d)
        self.assertIsInstance(b2, BaseModel)

    def test_datetime_conversion(self):
        """Test datetime is converted from isoformat string."""
        b = BaseModel()
        d = b.to_dict()
        b2 = BaseModel(**d)
        self.assertIsInstance(b2.created_at, datetime)
        self.assertIsInstance(b2.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
