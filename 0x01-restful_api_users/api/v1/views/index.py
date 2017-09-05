#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def status():
    """route /api/v1/status returns - status"""
    return jsonify(status="OK")
