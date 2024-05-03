#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from models import amenity, base_model, city, place, review, state, user
from datetime import datetime

to_json = base_model.BaseModel.to_json
strptime = datetime.strptime

class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""
    CNC = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
        }
    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in FileStorage.__objects.items():
                if type(value).__name__ == cls:
                    new_dict[key] = value
            return new_dict
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fname = FileStorage.__file_path
        json_objects = {}
        for key, k_id in FileStorage.__objects.items():
            json_objects[key] = key.to_json()
        with open(fname, mode='w+', encoding='utf-8') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        fname =  FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(fname, mode='r', encoding='utf-8') as f:
                jo = json.load(f)
        except:
            return
        for old, b in jo.items():
            b_cls = b['__class__']
            b.pop("__class__", None)
            b["created_at"] = datetime.strptime(b["created_at"],
                                                "%Y-%m-%d %H:%M:%S.%f")
            b["updated_at"] = datetime.strptime(b["updated_at"],
                                                "%Y-%m-%d %H:%M:%S.%f")
            FileStorage.__objects[old] = FileStorage.CNC[b_cls](**b)

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is None:
            return
        for a in list(FileStorage.__objects.keys()):    
            if obj.id == a.split(".")[1] and a.split(".")[0] in str(obj):
                FileStorage.__objects.pop(a, None)
                self.save()

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """returns the object based on the class and its ID,
        or None if not found"""
        all_cls = self.all(cls)
        for obj in all_cls.values():
            if id == str(obj.id):
                return obj

        return None

    def count(self, cls=None):
        """returns the number of objects in storage matching the given class.
        If no class is passed, returns the count of all objects in storage."""
        return len(self.all(cls))