#!/usr/bin/python3
"""
users view with routes
 GET /users -  list of users
 GET /users/<user_id> - fetches user with user_id
 DELETE /users/<user_id> - fetches {}
 POST /users - creates a user
 PUT /users/<user_id> - update a user with user_id
"""
from flask import Flask, abort, request
from flask import jsonify
from api.v1.views import app_views
from models import User, db_session


@app_views.route('/users', strict_slashes=False, methods=['GET'])
def users():
    """route /api/v1/users returns - list of users"""
    users = []
    for user in User.all():
        users.append(user.to_dict())
    return jsonify(users)


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['GET'])
def get_user(user_id):
    """route /users/<user_id> returns - user with user_id

    :param user_id: user id of user to fetch

    """
    user = User.get(user_id)
    if user is None:
        return abort(404)
    else:
        return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['DELETE'])
def delete_user(user_id):
    """route /users/<user_id> returns - {}

    :param user_id: user id of user to be deleted

    """
    user = User.get(user_id)
    if user is None:
        return abort(404)
    else:
        db_session.delete(user)
        db_session.commit()
        return jsonify()


@app_views.route('/users', strict_slashes=False, methods=['POST'])
def create_user():
    """route /users returns - created user"""
    if request.get_json():
        json = request.get_json()
        email = json.get('email')
        password = json.get('password')
        if email is None:
            return jsonify(error="email missing"), 400
        if password is None:
            return jsonify(error="password missing"), 400
        newUser = User()
        newUser.email = json['email']
        newUser.password = json['password']
        if json.get('first_name'):
            newUser.first_name = json.get('first_name')
        if json.get('last_name'):
            newUser.last_name = json.get('last_name')
        try:
            db_session.add(newUser)
            db_session.commit()
        except BaseException:
            return jsonify(error="Can't create User: <exception message>"), 400
        return jsonify(User.last().to_dict()), 201
    else:
        return jsonify(error="Wrong format"), 400


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['PUT'])
def update_user(user_id):
    """route /users/<user_id> returns - updated user

    :param user_id: user id of user to be deleted

    """
    user = User.get(user_id)
    if user is None:
        return abort(404)
    if request.get_json():
        json = request.get_json()
        if json.get('first_name'):
            user.first_name = json['first_name']
        if json.get('last_name'):
            user.last_name = json['last_name']
        db_session.commit()
        return jsonify(user.to_dict())
    else:
        return jsonify(error="Wrong format"), 400
