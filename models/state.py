#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
storage_type = environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """Representation of state """
    if storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

    if storage_type != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
