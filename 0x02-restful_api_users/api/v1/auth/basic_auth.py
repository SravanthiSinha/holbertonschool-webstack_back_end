#!/usr/bin/python3
"""A class to manage the API authentication"""
from flask import Flask
from flask import request
from api.v1.auth.auth import Auth
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
