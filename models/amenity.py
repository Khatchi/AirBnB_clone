#!/usr/bin/python3
"""This modules creates the amenity's class that
inherits from the BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class manages the Amenity's objects.
    """

    name = ""
