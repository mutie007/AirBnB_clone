#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel."""

    def test_init(self):
        """Test initialization of BaseModel."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method."""
        model = BaseModel()
        string = str(model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(model.id, string)

    def test_save(self):
        """Test the save method."""
        model = BaseModel()
        old_updated = model.updated_at
        model.save()
        self.assertNotEqual(old_updated, model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertEqual(model_dict["id"], model.id)

    def test_init_from_dict(self):
        """Test recreation of instance from dictionary."""
        model = BaseModel()
        model.name = "Test"
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)
        self.assertFalse(model is new_model)


if __name__ == "__main__":
    unittest.main()
