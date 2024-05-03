#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String, ForeignKey, Float, Integer

storage_type = environ.get("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """Representation of Review """
    __tablename__ = 'reviews'
    if storage_type == 'db':
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
