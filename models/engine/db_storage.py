#!/usr/bin/python3
"""
Contains the class DBStorage
"""
from models import amenity, base_model, city, place, review, state, user
from os import environ
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """interacts with the MySQL database"""
    CNC = { 
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': review.Review,
        'State': state.State,
        'User': user.User
    }
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = environ.get('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = environ.get('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = environ.get('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = environ.get('HBNB_MYSQL_DB')
        HBNB_ENV = environ.get('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        if cls:
            objs = self.__session.query(self.CNC.get(cls)).all()
            for obj in objs:
                key = str(obj.__class__.__name__) + '.' + str(obj.id)
                new_dict[key] = obj
            return (new_dict)
        for cls_name in self.CNC:
            if cls_name == 'BaseModel':
                continue
            objs = self.__session.query(self.CNC.get(cls_name)).all()
            for obj in objs:
                key = str(obj.__class__.__name__) + '.' + str(obj.id)
                new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """Gets back an object by class and ID
        :param cls: Class
        :param id: ID of obj
        :return: obj or None
        """
        all_cls = self.all(cls)
        for obj in all_cls.values():
            if id == str(obj.id):
                return obj

        return None

    def count(self, cls=None):
        """Counts objects in storage based on a specified class; if no class is provided,
        counts all stored objects"""
        return len(self.all(cls))
