#!/usr/bin/python3
"""This module creates a User class that inherits from
the BaseModel class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class manages User objects.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
