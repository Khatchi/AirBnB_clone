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

    def Classes(self):
        """This function returns the dictionary of all the
        classes with their references.
        The classes previously created are imported and the class
        names used both as the key and value.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        classes = {"BaseModel": BaseModel, "User": User,
                   "State": State, "City": City,
                   "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        return (Classes)

    def attributes(self):
        """This func. returns valid attribute and the
        correcponding type for each classname in a nested dic.
        """

        attributes = {
                "BaseModel": {"id": str,
                              "created_at": datetime.datetime,
                              "updated_at": datetime.datetime
                              },
                "User": {"email": str,
                         "password": str,
                         "first_name": str,
                         "last_name": str
                         },
                "Sate": {"name": str
                         }
                "City": {"state_id": str,
                         "name": str
                         },
                "Amenity": {"name": str
                            },
                "Place": {"city_id": str,
                          "user.id": str,
                          "name": str,
                          "description": str,
                          "number_rooms": int,
                          "number_bathrooms": int,
                          "max_guest": int,
                          "price_by_night": int,
                          "latidude": float,
                          "longitude": float,
                          "amenity_ids": list
                          },
                "Review": {"place_id": str,
                           "user_id": str,
                           "text": str
                           }
                }
        return (attributes)
