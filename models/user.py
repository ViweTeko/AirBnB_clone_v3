#!/usr/bin/python3
""" holds class User"""
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from hashlib import md5
storage_type = environ.get('HBNB_TYPE_STORAGE')


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

    @property
    def password(self):
        """ Password getter
        :return: (hashed) password """
        return self.__dict__.get("password")

    @password.setter
    def password(self, password):
        """ Password setter with md5 hashing
        :param password: password """
        self.__dict__["password"] = md5(password.encode('utf-8')).hexdigest()
