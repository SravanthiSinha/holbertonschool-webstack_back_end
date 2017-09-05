#!/usr/bin/python3
import hashlib
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime

"""
This is the user module.
This is a User class inside the user module (inherits BaseModel and Base).
"""


class User(BaseModel, Base):
    """This is a User class"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    _password = Column("password", String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __str__(self):
        """override to return [User] {id} - {email} - {display_name()}"""
        return "[{}] {} - {} - {}".format(self.__class__.__name__, self.id,
                                          self.email, self.display_name())

    @property
    def password(self):
        """Retrieve _password"""
        return self._password

    @password.setter
    def password(self, password):
        """Takes a string, and encrypts it with the MD5 algorithm.
        and assigns this new value, lowercase, to _password

        :param password: the password to be set

        """
        if password is None or not isinstance(password, str):
            self._password = None
        else:
            m = hashlib.md5()
            m.update(password.encode('utf-8'))
            self._password = m.hexdigest().lower()

    def display_name(self):
        """Displays the full name of an User instance


        :returns: If email, first_name and last_name are equal to None
        * If first_name and last_name are equal to None, return the email
        * If last_name is equal to None, return the first_name
        * If first_name is equal to None, return the last_name
        * Otherwise: return {first_name} {last_name}

        """
        if(self.email is None):
            if(self.first_name is None and self.last_name is None):
                return ""
        if(self.first_name is None and self.last_name is None):
            return self.email
        if(self.last_name is None):
            return self.first_name
        if(self.first_name is None):
            return self.last_name
        return "%s %s" % (self.first_name, self.last_name)

    def is_valid_password(self, pwd):
        """validates that the value passed is the clear version of the password
        of a User instance

        :param pwd: pwd to be checked with

        """
        if pwd is None:
            return False
        if not isinstance(pwd, str):
            return False
        if self._password is None:
            return False
        if self._password == hashlib.md5(pwd.encode()).hexdigest().lower():
            return True
        return False

    def to_dict(self):
        """serialize User"""
        user_to_dict = {
            "id": str(self.id),
            "email": str(self.email),
            "first_name": str(self.first_name),
            "last_name": str(self.last_name),
            "created_at": str(datetime.strftime(
                self.created_at, "%Y-%m-%d %H:%M:%S"
            )
            ),
            "updated_at": str(datetime.strftime(
                self.updated_at, "%Y-%m-%d %H:%M:%S"
            )
            )
        }
        return user_to_dict
