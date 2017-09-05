#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/c', strict_slashes=False, methods=['GET'])
def c():
    """route /c returns - C is fun!"""
    return "C is fun!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
