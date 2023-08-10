#!/usr/bin/python3
"""
This script contains the BaseModel class which contains
contains all elements(attributes and method)common to all the
subclasses.
"""

import uuid
from datetime import datetime
from models import storage

"""The uuid modules provides functionality to generate universally unique
identifiers(uuids).
The datetime module provides various methods for creating
and manipulating datetime objects.
The storage module handles data storage and retrieval.
"""


class BaseModel:

    """This is the base class which provides shared functionality from which
    other subclasses inherit from.
    """

    def __init__(self, *args, **kwargs):
        """Defines a constructor which initializes instance attributes.

        Args:
            --> *args: parameter that accepts list of arguments
            --> **kwargs: parameter that accept additionaly key-word
                arguments as dict.
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strftime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strftime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
            else:
                self.id = str(_uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                storage.new(self)

    def __str__(self):
        """This function(method) returns the string represenation
        of the objects.
        """

        return "[{}] ({} {})".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """A func. that updates the pub instance attr updated_at
        to the currect time stamp.
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """A func. that returns the key with the corresponding values
        of a __dict__.
        """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()

        return (my_dict)
