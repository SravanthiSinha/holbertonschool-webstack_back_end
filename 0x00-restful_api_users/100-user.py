#!/usr/bin/python3
"""
Test all() on User instance (inherits from BaseModel)
"""
from models.user import User

for user in User.all():
    print(user)
