#!/usr/bin/python3
"""A class to manage the API authentication"""
from flask import Flask
from flask import request
"""
This is the Auth module.
This is a Auth class inside the auth module.
"""


class Auth():
    """A class to manage the API authentication"""

    def require_auth(self, path, excluded_paths):
        """require authorization

        :param path: Unknown
        :param excluded_paths: Unknown

        """
        return False

    def authorization_header(self, request=None):
        """Handles Authorization Header

        :param request: Flask request object (Default value = None)

        """
        return None

    def current_user(self, request=None):
        """Handles current user

        :param request: Flask request object (Default value = None)

        """
        return None
