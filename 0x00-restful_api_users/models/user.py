#!/usr/bin/python3
from models.base_model import BaseModel
"""
This is the user module.
This is a User class inside the user module (inherits BaseModel).
"""


class User(BaseModel):
    """
    This is a User class
    """
    email = None
    first_name = None
    last_name = None
    _password = None
