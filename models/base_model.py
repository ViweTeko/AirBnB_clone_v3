#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
import models
from os import environ
from sqlalchemy import Column, String, DateTime, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4, UUID

storage_type = environ.get('HBNB_TYPE_STORAGE')

if storage_type == "db":
    Base = declarative_base()
else:
    class Base:
        pass


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    if storage_type == "db":
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def bm_update(self, name, val):
        """ Updates BaseModel and sets correct attrs """
        setattr(self, name, val)
        if storage_type != 'db':
            self.save()

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        if storage_type != 'db':    
            self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_json(self):
        """returns json rep of self"""
        new_dict = {}
        for key, val in (self.__dict__).items():
            if (self.__is_serializable(val)):
                new_dict[key] = val
            else:
                new_dict[key] = str(val)
        new_dict['__class__'] = type(self).__name__
        if '_sa_instance_state' in new_dict:
            new_dict.pop('_sa_instance_state')
        if storage_type == 'db' and 'password' in new_dict:
            new_dict.pop('password')
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        self.delete()

    def __str__(self):
        """Returns string type rep of obj instance """
        cls_name = type(self).__name__
        return '[{}] ({}) {}'.format(cls_name, self.id, self.__dict__)

    def __is_serializable(self, obj_v):
        """ Private: checks if obj is serializable """
        try:
            obj_str = json.dumps(obj_v)
            return obj_str is not None  and isinstance(obj_str, str)
        except:
            return False