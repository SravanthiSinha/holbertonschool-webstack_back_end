#!/usr/bin/python3
"""A class to manage the API authentication"""
from flask import Flask
from flask import request
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta
"""
This is the session_exp_auth module.
This is a SessionExpAuth class inside the session_exp_auth module.
"""


class SessionExpAuth(SessionAuth):
    """A class to manage the expiration of Session Authentication"""

    def __init__(self):
        duration = 0
        try:
            duration = int(getenv('HBNB_YELP_SESSION_DURATION'))
        except ValueError:
            pass
        self.session_duration = duration

    def create_session(self, user_id=None):
        """
        Overloading
        :param user_id:  (Default value = None)

        """
        session_id = super(SessionExpAuth, self).create_session(user_id)
        if session_id is None:
            None
        user_id = self.user_id_by_session_id.get(session_id)
        my_dict = {'user_id': user_id, 'created_at': datetime.now()}
        self.user_id_by_session_id[session_id] = my_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Overloading
        :param session_id:  (Default value = None)

        """
        if session_id is None:
            return None
        my_dict = self.user_id_by_session_id.get(session_id)
        if my_dict.get('user_id') is None:
            return None
        if self.session_duration <= 0:
            return user_id
        created_at = my_dict.get('created_at')
        if created_at is None:
            return None
        elapsed = datetime.now() - created_at
        if elapsed > timedelta(seconds=self.session_duration):
            return None
        return my_dict.get('user_id')
