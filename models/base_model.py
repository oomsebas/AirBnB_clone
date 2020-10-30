#!/usr/bin/python3
""" BaseModel that defines all common attributes/methods for other classes """


import uuid
import datetime
from models.__init__ import storage


class BaseModel:
    """
    Base model class, this class returns a representation dict of  an instance
    """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        if kwargs:
            for key, value in kwargs.items():
                if key is  "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                   exec("self." + key + "= datetime.datetime.strptime( \"" + value + "\", \"%Y-%m-%dT%H:%M:%S.%f\")")
                else:
                    self.key = value
        else:
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            storage.new(self)

    def __str__(self):
        return "[" + str(self.__class__.__name__) + "]" + " (" + self.id + ")"\
            + " " + str( self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        dictcpy = self.__dict__.copy()
        dictcpy["__class__"] = str(self.__class__.__name__)
        dictcpy["created_at"] = datetime.datetime.isoformat(self.created_at)
        dictcpy["updated_at"] = datetime.datetime.isoformat(self.updated_at)
        return dictcpy
