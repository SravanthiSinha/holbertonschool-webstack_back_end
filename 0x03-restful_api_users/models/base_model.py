#!/usr/bin/python3
"""
This is the base_model module.
This is a BaseModel class inside the base_model module.
"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, desc


Base = declarative_base()


class BaseModel:
    """This is a BaseModel class"""
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow(),
                        onupdate=datetime.utcnow())

    def __init__(self):
        """Initializes the BaseModel with id, created_at, updated_at"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    @classmethod
    def all(cls):
        """Returns all instances of the cls from the database"""
        from models import db_session
        query = db_session.query(cls).order_by(cls.created_at).all()
        return(query)

    @classmethod
    def count(cls):
        """Returns allthe number instances of cls objects in the database"""
        from models import db_session
        query = db_session.query(cls).count()
        return(query)

    @classmethod
    def get(cls, id):
        """Returns an instance of cls with a specific id.
           Returns None if the id passed is None or not a string

        :param id: id to be retrieved

        """
        from models import db_session

        if id is None or not isinstance(id, str):
            return (None)

        query = db_session.query(cls).get(id)
        return (query)

    @classmethod
    def first(cls):
        """Returns the first instance of cls from database"""
        from models import db_session

        query = db_session.query(cls).order_by(cls.created_at).first()
        return(query)

    @classmethod
    def last(cls):
        """Returns the last instance of cls from database"""
        from models import db_session

        query = db_session.query(cls).order_by(desc(cls.created_at)).first()
        return(query)
