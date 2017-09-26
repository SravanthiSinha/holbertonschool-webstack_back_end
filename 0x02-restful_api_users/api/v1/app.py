#!/usr/bin/python3
"""A script that start a Flask application and handles database and errors"""
from flask import Flask
from flask import jsonify
from os import getenv
from api.v1.views import app_views
from models import db_session

env_port = getenv('HBNB_API_PORT')
env_host = getenv('HBNB_API_HOST')

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    """error handler for 404 error

    :param e: unused

    """
    return jsonify(error="Not found"), 404


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
