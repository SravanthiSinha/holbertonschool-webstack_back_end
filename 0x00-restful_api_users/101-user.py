#!/usr/bin/python3
"""
Test count() on User instance (inherits from BaseModel)
"""
from models.user import User

print(User.count())
