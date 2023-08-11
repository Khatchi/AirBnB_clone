#!/usr/bin/python3
"""This module creates the Review class that inherits
from the BaseModel class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class manages the Review's objects.
    """

    place_id = ""
    user_id = ""
    text = ""
