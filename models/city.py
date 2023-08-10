#!/usr/bin/python3
"""This module creats the City class that
inherits from the BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class manages City's objects.
    """

    state_id = ""
    name = ""
