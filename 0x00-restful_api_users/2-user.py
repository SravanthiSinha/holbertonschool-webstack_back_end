#!/usr/bin/python3
"""
Test display_name() on User instance
"""
from models.user import User

user = User()
user.email = "hbtn@holbertonschool.com"
print(user.display_name())

user.first_name = "Bob"
print(user.display_name())

user.last_name = "Dylan"
print(user.display_name())
