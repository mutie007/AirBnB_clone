#!/usr/bin/python3
"""Unit tests for FileStorage class."""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage."""

    def test_instance(self):
        """Test FileStorage instance."""
        f = FileStorage()
        self.assertIsInstance(f, FileStorage)

    def test_file_path_is_private(self):
        """Test __file_path is private string."""
        self.assertIsInstance(
            FileStorage._FileStorage__file_path, str)

    def test_objects_is_private(self):
        """Test __objects is private dict."""
        self.assertIsInstance(
            FileStorage._FileStorage__objects, dict)

    def test_all_returns_dict(self):
        """Test all() returns a dictionary."""
        result = storage.all()
        self.assertIsInstance(result, dict)

    def test_new(self):
        """Test new() adds object to __objects."""
        b = BaseModel()
        storage.new(b)
        key = "BaseModel.{}".format(b.id)
        self.assertIn(key, storage.all())

    def test_save_creates_file(self):
        """Test save() creates file.json."""
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test reload() loads objects from file."""
        b = BaseModel()
        storage.new(b)
        storage.save()
        storage.reload()
        key = "BaseModel.{}".format(b.id)
        self.assertIn(key, storage.all())

    def test_storage_is_filestorage(self):
        """Test storage is FileStorage instance."""
        self.assertIsInstance(storage, FileStorage)

    def test_file_path_value(self):
        """Test __file_path is file.json."""
        self.assertEqual(
            FileStorage._FileStorage__file_path, "file.json")


if __name__ == "__main__":
    unittest.main()
