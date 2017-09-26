#!/usr/bin/python3
"""index view with /status and /stats as routes """
from flask import Flask
from flask import jsonify
from api.v1.views import app_views
from models import User


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def status():
    """route /api/v1/status returns - status"""
    return jsonify(status="OK")


@app_views.route('/stats', strict_slashes=False, methods=['GET'])
def stats():
    """route /api/v1/status returns - count of users"""
    return jsonify(users=User.count())
