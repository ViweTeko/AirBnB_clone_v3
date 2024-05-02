#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey, Float, Integer
storage_type = os.environ.get("HBNB_STORSGE_TYPE")


class Review(BaseModel, Base):
    """Representation of Review """
    if storage_type == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
