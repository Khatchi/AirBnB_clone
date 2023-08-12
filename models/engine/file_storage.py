#!/usr/bin/python3
"""
file storage module

"""

from json import load, dump, dumps
from os.path import exists
from models import base_model, user, place, state, city, amenity, review

BaseModel = base_model.BaseModel
User = user.User
Place = place.Place
State = state.State
City = city.City
Amenity = amenity.Amenity
Review = review.Review

name_class = ["BaseModel", "City", "State",
              "Place", "Amenity", "Review", "User"]


class FileStorage():
    """ FileStorage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns all objects in file storage """

        return self.__objects

    def new(self, obj):
        """ creates a new object """

        class_name = obj.__class__.__name__
        class_id = class_name + "." + obj.id
        self.__objects[class_id] = obj

    def save(self):
        """ stores object data to a json file """

        dict_to_json = {}
        for key, value in self.__objects.items():
            dict_to_json[key] = value.to_dict()
            with open(self.__file_path, "w", encoding="utf-8") as file:
                dump(dict_to_json, file)

    def reload(self):
        """ loads data from a json file and then stores in a dictionary """

        json_to_dict = {}
        if (exists(self.__file_path)):
            with open(self.__file_path, "r") as file:
                json_to_dict = load(file)
                for key, value in json_to_dict.items():
                    class_name = key.split(".")[0]
                    if class_name in name_class:
                        FileStorage.__objects[key] = eval(class_name)(**value)
                    else:
                        pass
