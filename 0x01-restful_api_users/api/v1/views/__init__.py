#!/usr/bin/python3
from flask import Blueprint


app_views = Blueprint(
    name="app_views",
    import_name=__name__,
    url_prefix="/api/v1")

try:
    from api.v1.views.index import *
    from api.v1.views.users import *
except BaseException:
    raise
