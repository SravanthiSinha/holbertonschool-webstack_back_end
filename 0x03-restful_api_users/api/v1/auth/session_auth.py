#!/usr/bin/python3
"""A class to manage the API authentication"""
from flask import Flask
from flask import request
from api.v1.auth.auth import Auth
from uuid import uuid4
from os import getenv
from models import db_session, User
"""
This is the session_auth module.
This is a SessionAuth class inside the session_auth module.
"""


class SessionAuth(Auth):
    """A class to manage the Session authentication"""
    user_id_by_session_id = dict()

    def create_session(self, user_id=None):
        """creates a Session ID for a user_id

        :param user_id: Default value = None

        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        if self.user_id_by_session_id.get(session_id) is None:
            self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """fetches a User ID based on a Session ID

        :param session_id: Default value = None

        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """fetches current_user based on a cookie value

        :param request: Default value = None)

        """
        cookie_name = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie_name)
        if user_id is not None:
            for user in db_session.query(User).filter(User.id == user_id):
                if not user:
                    return None
                return user

    def destroy_session(self, request=None):
        """Deletes the user session

        :param request:  (Default value = None)

        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        self.user_id_by_session_id.pop(session_id, None)
        return True
