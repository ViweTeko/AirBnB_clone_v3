#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String, ForeignKey, Float, Integer
from sqlalchemy.orm import relationship
storage_type = environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """Representation of city """
    if storage_type == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="delete")
    else:
        state_id = ""
        name = ""

    if storage_type != 'db':
        @property
        def places(self):
            """Getter city"""
            all_places = models.storage.all("Place")
            result = []

            for obj in all_places.values():
                if str(obj.city_id) == str(self.id):
                    result.append(obj)
            return result