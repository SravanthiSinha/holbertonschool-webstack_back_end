#!/usr/bin/python3
"""A script that start a Flask application"""
from flask import Flask
from flask import jsonify
from os import getenv


app = Flask(__name__)
env_port = getenv('HBNB_API_PORT')
env_host = getenv('HBNB_API_HOST')


@app.route('/hbtn', strict_slashes=False, methods=['GET'])
def hbtn():
    """route /hbtn returns - json data"""
    return jsonify(C="is fun", Python="is cool", sysadmin="is hiring")


if __name__ == '__main__':
    if(env_port is not None and env_host is not None):
        app.run(host=env_host, port=int(env_port), debug=True)
    else:
        app.run(debug=True)
