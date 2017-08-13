#!/usr/bin/python3
"""
Test get() on User instance (inherits from BaseModel)
"""
from models.user import User

for user in User.all():
    print(User.get(user.id))
