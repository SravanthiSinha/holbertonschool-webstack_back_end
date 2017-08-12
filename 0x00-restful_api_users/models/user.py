#!/usr/bin/python3
from models.base_model import BaseModel
"""
This is the user module.
This is a User class inside the user module (inherits BaseModel).
"""


class User(BaseModel):
    """This is a User class"""
    email = None
    first_name = None
    last_name = None
    _password = None

    def display_name(self):
        """Displays the full name of an User instance


        :returns:
        * If email, first_name and last_name are equal to None
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
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        """override to return [User] {id} - {email} - {display_name()}"""
        op = "[User] %s - %s - %s" % (self.id, self.email, self.display_name())
        return op
