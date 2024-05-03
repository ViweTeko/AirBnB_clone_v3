#!/usr/bin/python3
"""
initialize the models package
"""
from os import environ
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


if environ.get("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    CNC = DBStorage.CNC
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    CNC = FileStorage.CNC
    storage = FileStorage()
storage.reload()