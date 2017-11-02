#!/usr/bin/python3
"""
 Handles all routes for the Session authentication
 POST /api/v1/auth_session/login
"""
from flask import Flask, abort, request
from flask import jsonify
from api.v1.views import app_views
from models import User, db_session
from api.v1.app import auth
from os import getenv


@app_views.route('/auth_session/login', strict_slashes=False, methods=['POST'])
def login():
    """route /auth_session/login"""
    user_email = request.form.get('email')
    user_pwd = request.form.get('password')
    print(user_email)
    if user_email is None:
        return jsonify(error="email missing"), 400
    if user_pwd is None:
        return jsonify(error="password missing"), 400
    for user in db_session.query(User).filter(User.email == user_email):
        if not user.is_valid_password(user_pwd):
            return jsonify(error="wrong password"), 401
        session_id = auth.create_session(user.id)
        out = jsonify(state=0, msg='success')
        out.set_cookie(getenv('HBNB_YELP_SESSION_NAME'), session_id)
        return jsonify(user.to_dict())
    return jsonify(error="no user found for this email"), 404
