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
        """ returns True if the path is not in the list of strings excluded_paths

        :param path: Unknown
        :param excluded_paths: Unknown

        """
        if (path is None) or (excluded_paths is None) or (not excluded_paths):
            return True
        for p in excluded_paths:
            if (p == path) or (p[::-1][0] == '/' and p[:-1] == path):
                return False
        return True

    def authorization_header(self, request=None):
        """Handles Authorization Header

        :param request: Flask request object (Default value = None)

        """
        if (request is None) or ('Authorization' not in request.headers):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None):
        """Handles current user

        :param request: Flask request object (Default value = None)

        """
        return None
