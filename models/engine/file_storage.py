#!/usr/bin/python3
"""This module defines the FileStorage class."""
import json
import os
import datetime


class FileStorage:
    """This class stores and retrieves data"""

    __file_path = "file.json"
    """Private class attr rep str-path to json file."""
    __objects = {}
    """Private class attr- an empty dict.that will store objects."""

    def all(self):
        """Pub. instance method that returns the dict obj(__objects)"""
        return (FileStorage.__objects)

    def new(self, obj):
        """A pub inst. that sets in __objects the obj with
        key <obj class name>.id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """A pub. inst that serializes __objects to JSON file-path:
        __file_path.
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserializes the JSON file to __objects, that is, reloads
        the stored objects.
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v) for k
                        k, v in obj_dict.items}

            FileStorage.__objects = obj_dict
