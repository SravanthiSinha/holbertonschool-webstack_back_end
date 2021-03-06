#!/usr/bin/python3
"""Creates an instance of Blueprint called app_views & imports all the views"""
from flask import Blueprint


app_views = Blueprint(
    name="app_views",
    import_name=__name__,
    url_prefix="/api/v1")

try:
    from api.v1.views.index import *
    from api.v1.views.users import *
    from api.v1.views.session_auth import *
except BaseException:
    raise
