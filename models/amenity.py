#!/usr/bin/python
""" holds class Amenity"""
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import relationship, backref
storage_type = environ.get('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if storage_type == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity")
    else:
        name = ""