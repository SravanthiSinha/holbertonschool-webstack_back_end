#!/usr/bin/python3
"""index view with /status and /stats as routes """
from flask import Flask, abort
from flask import jsonify
from api.v1.views import app_views
from models import User


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def status():
    """route /api/v1/status returns - status"""
    return jsonify(status="OK")


@app_views.route('/stats', strict_slashes=False, methods=['GET'])
def stats():
    """route /api/v1/stats returns - count of users"""
    return jsonify(users=User.count())


@app_views.route('/unauthorized', strict_slashes=False, methods=['GET'])
def unauthorized():
    """route /api/v1/unauthorized returns - custom error"""
    return abort(401)


@app_views.route('/forbidden', strict_slashes=False, methods=['GET'])
def forbidden():
    """route /api/v1/forbidden returns - custom error"""
    return abort(403)
