#!/usr/bin/python3
"""
Test password on User instance
"""
from models.user import User

user = User()
user.password = "hello"
print(user.password)

user.password = "hello world"
print(user.password)
