#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
"""
This is the base_model module.
This is a BaseModel class inside the base_model module.
"""


class BaseModel:
    """This is a BaseModel class"""
    id = None
    created_at = None
    updated_at = None

    def __init__(self):
        """Initializes the BaseModel with id, created_at, updated_at"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
