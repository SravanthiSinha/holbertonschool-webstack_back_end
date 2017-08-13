#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

"""
This is the base_model module.
This is a BaseModel class inside the base_model module.
"""

Base = declarative_base()


class BaseModel:
    """This is a BaseModel class"""
    id = Column(String(60), nullable=False, primary_key=True)
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
