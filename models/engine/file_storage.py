#!/usr/bin/pyhton3
""" recreate a BaseModel from another one by using a dictionary representation"""

import json
import os

class FileStorage:
    """This class saves in a file  the representation models in JSON format.
       serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        name = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[name] = str(obj)

    def save(self):
        with open(FileStorage.__file_path, "w") as _file:
           _file.write(json.dumps(FileStorage.__objects))

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as _file:
                FileStorage.__objects = json.load(_file)
