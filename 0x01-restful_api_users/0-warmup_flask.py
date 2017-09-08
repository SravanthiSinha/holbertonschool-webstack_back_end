#!/usr/bin/python3
"""A script that start a Flask application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False, methods=['GET'])
def index():
    """route / returns - Holberton School"""
    return 'Holberton School'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
