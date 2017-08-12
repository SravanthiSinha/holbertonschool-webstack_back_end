#!/usr/bin/python3
"""
Test __str__() on User instance
"""
from models.user import User

user = User()
user.email = "hbtn@holbertonschool.com"
print(user)

user.first_name = "Bob"
user.last_name = "Dylan"
print(user)
