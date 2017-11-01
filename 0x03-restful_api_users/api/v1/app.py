#!/usr/bin/python3
"""A script that start a Flask application and handles database and errors"""
from flask import Flask, abort
from flask import jsonify
from os import getenv
from api.v1.views import app_views
from models import db_session
from api.v1.auth.auth import Auth
from flask import request

env_port = getenv('HBNB_API_PORT')
env_host = getenv('HBNB_API_HOST')
env_auth = getenv('HBNB_YELP_AUTH')

app = Flask(__name__)
app.register_blueprint(app_views)

if env_auth == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif env_auth == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
else:
    auth = Auth()


@app.before_request
def before_request():
    """checks valid request paths on every request and sets the current user """
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']
    if auth.require_auth(request.path, excluded_paths):
        if auth.authorization_header(request) is None:
            abort(401)
        request.current_user = auth.current_user(request)
        if request.current_user is None:
            abort(403)
        
@app.errorhandler(404)
def page_not_found(e):
    """error handler for 404 error

    :param e: unused

    """
    return jsonify(error="Not found"), 404


@app.errorhandler(401)
def handle_unauthorized(e):
    """error handler for 401 error

    :param e: unused

    """
    return jsonify(error="Unauthorized"), 401


@app.errorhandler(403)
def handle_forbidden(e):
    """error handler for 403 error

    :param e: unused

    """
    return jsonify(error="Forbidden"), 403


@app.teardown_appcontext
def close_db(error):
    """Closes the database session at the end of the request.

    :param error: unused

    """
    db_session.remove()


if __name__ == '__main__':
    if(env_port is not None and env_host is not None):
        app.run(host=env_host, port=int(env_port))
    else:
        app.run()
