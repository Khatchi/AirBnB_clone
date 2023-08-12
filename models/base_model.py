#!/usr/bin/python3
""" Module for Base """
import uuid
from uuid import uuid4
from datetime import datetime
import models
import json
date_now = datetime.now()

format_dt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Initialization of Database """
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, format_dt)
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = date_now
            models.storage.new(self)

    def __str__(self):
        """ str definition """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ save definition """
        self.updated_at = date_now
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ to_dict definition """
        dic = {}
        for key, item in self.__dict__.items():
            dic[key] = item
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
