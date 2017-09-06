#!/usr/bin/python3
from flask import Flask, abort
from flask import jsonify
from api.v1.views import app_views
from models import User


@app_views.route('/users', strict_slashes=False, methods=['GET'])
def users():
    """route /api/v1/users returns - list of users"""
    users = []
    for user in User.all():
        users.append(user.to_dict())
    return jsonify(users)


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['GET'])
def get_user(user_id):
    """route /api/v1/status returns - user with user_id

    :param user_id: user id of user to fetch

    """
    user = User.get(user_id)
    if user is None:
        return abort(404)
    else:
        return jsonify(user.to_dict())
