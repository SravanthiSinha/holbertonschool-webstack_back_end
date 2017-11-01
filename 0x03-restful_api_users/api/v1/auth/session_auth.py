#!/usr/bin/python3
"""A class to manage the API authentication"""
from flask import Flask
from flask import request
from api.v1.auth.auth import Auth
import base64
"""
This is the session_auth module.
This is a SessionAuth class inside the session_auth module.
"""


class SessionAuth(Auth):
    """A class to manage the Session authentication"""
    pass
