#!/usr/bin/env python3
"""Module that handles all routes for Session authentication"""

import os
from typing import Tuple
from models.user import User
from api.v1.views import app_views
from flask import abort, jsonify, request


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Tuple[str, int]:
    """Handles user login"""

    user_email = request.form.get('email')
    user_pswd = request.form.get('password')

    if user_email is None or user_email == '':
        return jsonify({"error": "email missing"}), 400
    if user_pswd is None or user_pswd == '':
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': user_email})
    if not users or users == []:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(user_pswd):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            resp = jsonify(user.to_json())
            session_name = os.getenv('SESSION_NAME')
            resp.set_cookie(session_name, session_id)
            return resp
    return jsonify({"error": "wrong password"}), 401


@app_views.route('aut_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """Handle user logout"""
    # Destroy the session and check if successful
    destroy = auth.destroy_session(request)
    if destroy is False:
        abort(404)

    # Return an empty JSON dictionary with status code 200
    return jsonify({}), 200
