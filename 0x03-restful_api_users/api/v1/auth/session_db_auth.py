#!/usr/bin/python3
"""A class to manage the DB for Session authentication"""
from flask import Flask
from flask import request
from api.v1.auth.session_exp_auth import SessionExpAuth
from models import db_session, UserSession
from datetime import datetime, timedelta
"""
This is the session_db_auth module.
This is a SessionDBAuth class inside the session_db_auth module.
"""


class SessionDBAuth(SessionExpAuth):
    """A class to manage the Database for Session Authentication"""

    def create_session(self, user_id=None):
        """Overloading

        :param user_id: Default value = None)

        """
        session_id = super(SessionDBAuth, self).create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession()
        user_session.user_id = user_id
        user_session.session_id = session_id
        try:
            db_session.add(user_session)
            db_session.commit()
        except BaseException:
            return None
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Overloading

        :param session_id: Default value = None)

        """
        if session_id is None:
            return None
        for user_session in db_session.query(UserSession).filter(
                UserSession.session_id == session_id):
            elapsed = datetime.utcnow() - user_session.created_at
            if elapsed > timedelta(seconds=self.session_duration):
                return None
            return user_session.user_id
        return None

    def destroy_session(self, request=None):
        """Overloading

        :param request: Default value = None)

        """
        session_id = self.session_cookie(request)
        if session_id and super(SessionDBAuth, self).destroy_session(request):
            for user_session in db_session.query(UserSession).filter(
                    UserSession.session_id == session_id):
                db_session.delete(user_session)
                db_session.commit()
                return True
        return False
