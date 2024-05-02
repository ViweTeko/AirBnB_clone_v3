#!/usr/bin/python3
""" holds class User"""
from models.base_model import BaseModel, Base
import os
import sqlalchemy
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from hashlib import md5
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """Representation of a user """
    if storage_type == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade='delete')
        reviews = relationship("Review", backref="user", cascade='delete')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
