#!/usr/bin/python3
"""
This is the user_session module.
This is a UserSession class inside the user_session module (inherits BaseModel
and Base).
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class UserSession(BaseModel, Base):
    """This is a UserSession class"""
    __tablename__ = "user_sessions"
    user_id = Column(String(60), nullable=False)
    session_id = Column(String(60), nullable=False)
