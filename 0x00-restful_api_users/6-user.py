#!/usr/bin/python3
"""
Test to_dict() on User instance
"""
from models.user import User

user = User()
user.email = "hbtn@holbertonschool.com"
user.password = "toto1234"
user.first_name = "Bob"
user.last_name = "Dylan"
d_user = user.to_dict()

for user_attribute in d_user.keys():
    print("{} ({}): {}".format(user_attribute, type(d_user[user_attribute]), d_user[user_attribute]))
