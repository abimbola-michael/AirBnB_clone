#!/usr/bin/python3
"""a class FileStorage that serializes instances """

import json
"""from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review"""


class FileStorage:
    """a class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path"""

        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict().copy()

        with open(FileStorage.__file_path, "w") as fl:
            json.dump(obj_dict, fl)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing"""

        try:
            with open(FileStorage.__file_path, "r") as fl:
                obj_dict = json.load(fl)
                for key, value in obj_dict.items():
                    FileStorage.__objects[key] = eval(
                            "".join([key.split(".")[0], "(**value)"])
                            )
        except FileNotFoundError:
            pass
