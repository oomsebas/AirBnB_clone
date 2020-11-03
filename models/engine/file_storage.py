#!/usr/bin/pyhton3
"""recreate a BaseModel from another one using a dictionary representation"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    This class saves in a file  the representation models in JSON format.
    serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        name = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[name] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        n_dict = {}
        for key, value in FileStorage.__objects.items():
            n_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as fd:
            json.dump(n_dict, fd)

    def reload(self):
        """ deserializes the JSON file to __objects otherwise, do nothing."""

        n_dic = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as _file:
                n_dic = json.load(_file)
            for key, value in n_dic.items():
                FileStorage.__objects[key] = BaseModel(**value)
