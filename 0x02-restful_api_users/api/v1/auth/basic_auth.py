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
