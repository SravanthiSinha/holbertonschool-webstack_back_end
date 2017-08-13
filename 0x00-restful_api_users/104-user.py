#!/usr/bin/python3
"""
Test last() on User instance (inherits from BaseModel)
"""
from models.user import User

print(User.last())
