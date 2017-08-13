#!/usr/bin/python3
"""
Test link to MySQL database
"""
from models import db_session
from models.user import User

user = User()
user.email = "hbtn@holbertonschool.com"
user.password = "toto1234"
print("New user: {}".format(user))
db_session.add(user)
db_session.commit()

print("All users:")
for user in db_session.query(User).all():
    print(user)
