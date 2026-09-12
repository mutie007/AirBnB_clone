#!/usr/bin/python3
"""FileStorage class for serializing and deserializing instances."""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects (if it exists)."""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            from models.base_model import BaseModel
            for key, value in obj_dict.items():
                if value["__class__"] == "BaseModel":
                    FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
