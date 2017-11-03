#!/usr/bin/python3
"""
This is the session_exp_auth module.
This is a SessionExpAuth class inside the session_exp_auth module.
"""
from flask import Flask
from flask import request
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """A class to manage the expiration of Session Authentication"""

    def __init__(self):
        duration = getenv('HBNB_YELP_SESSION_DURATION')
        if duration is not None:
            self.session_duration = int(duration)
        else:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Overloading
        :param user_id:  (Default value = None)

        """
        if user_id is not None:
            session_id = super(SessionExpAuth, self).create_session(user_id)
            if session_id is None:
                None
            user_id = self.user_id_by_session_id.get(session_id)
            sesson_dict = {'user_id': user_id, 'created_at': datetime.now()}
            self.user_id_by_session_id[session_id] = sesson_dict
            return session_id
        return None

    def user_id_for_session_id(self, session_id=None):
        """
        Overloading
        :param session_id:  (Default value = None)

        """
        if session_id is None:
            return None
        sesson_dict = self.user_id_by_session_id.get(session_id)
        if sesson_dict is not None:
            if sesson_dict.get('user_id') is None:
                return None
            if self.session_duration <= 0:
                return sesson_dict.get('user_id')
            created_at = sesson_dict.get('created_at')
            if created_at is None:
                return None
            elapsed = datetime.now() - created_at
            if elapsed > timedelta(seconds=self.session_duration):
                return None
            return sesson_dict.get('user_id')
        return None
