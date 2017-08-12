#!/usr/bin/python3
"""
Test User class
"""
from models.user import User

user_1 = User()
print(user_1.id)
print(user_1.created_at)
print(user_1.updated_at)

user_2 = User()
print(user_2.id)
print(user_2.created_at)
print(user_2.updated_at)
