#!/usr/bin/python3
import hashlib
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime

"""
This is the user_session module.
This is a UserSession class inside the user_session module (inherits BaseModel
and Base).
"""


class UserSession(BaseModel, Base):
    """This is a UserSession class"""
    __tablename__ = "user_sessions"
    user_id = Column(String(60), nullable=False)
    session_id = Column(String(60), nullable=False)
