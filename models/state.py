#!/usr/bin/python3
"""This module creates the State class that
inherits from the BaseModel class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """This class manages the State objects.
    """

    name = ""
