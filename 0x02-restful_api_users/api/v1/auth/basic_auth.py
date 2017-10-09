#!/usr/bin/python3
"""A class to manage the API authentication"""
from flask import Flask
from flask import request
from api.v1.auth.auth import Auth
import base64
from models import db_session, User
"""
This is the basic_auth module.
This is a BasicAuth class inside the basic_auth module.
"""


class BasicAuth(Auth):
    """A class to manage the Basic authentication"""

    def extract_base64_authorization_header(self, authorization_header):
        """returns the Base64 part of the Authorization header

        :param authorization_header: contains Authorization header

        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.find('Basic') != 0:
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header):
        """returns the decoded value of a Base64 string
        base64_authorization_header

        :param base64_authorization_header: authorization header to be decoded

        """

        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            data = base64.b64decode(
                base64_authorization_header).decode('utf-8')
            return data
        except Exception as e:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header):
        """returns the user email and password from the Base64 decoded value

        :param decoded_base64_authorization_header: decoded base64 str of
        authorization header

        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if decoded_base64_authorization_header.find(":") == -1:
            return None, None
        credentails = decoded_base64_authorization_header.split(":")
        return credentails[0], credentails[1]

    def user_object_from_credentials(self, user_email, user_pwd):
        """returns the User instance based on email and password

        :param user_email: user email id
        :param user_pwd: user password

        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        for user in db_session.query(User).filter(User.email == user_email):
            if not user:
                return None
            if not user.is_valid_password(user_pwd):
                return None
            return user

    def current_user(self, request=None):
        """get current user on request with basic authentication

        :param request: Default value = None)

        """
        authorization_header = self.authorization_header(request)
        base64_authorization_header = self.extract_base64_authorization_header(
            authorization_header
        )
        decoded_base64 = self.decode_base64_authorization_header(
            base64_authorization_header)
        extracted_credentials = self.extract_user_credentials(decoded_base64)
        user_email = extracted_credentials[0]
        user_password = extracted_credentials[-1]
        user = self.user_object_from_credentials(
            user_email, user_password
        )
        return user
