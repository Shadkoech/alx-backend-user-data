#!/usr/bin/env python3
"""Module that sets up a flask app"""

from auth import Auth
from flask import Flask, jsonify, request, abort

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Route handler for the root URL ('/')"""
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


@app.route('/users', methods=['POST'])
def users():
    """Endpoint to register a user"""
    try:
        email = request.form['email']
        password = request.form['password']
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Endpoint to login user based on provided email & password
    Returns:
        JSON response with session ID, otherwise abort"""

    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(401)

    session_id = AUTH.create_session(email)
    if session_id:
        msg = {"email": email, "message": "logged in"}
        response = jsonify(msg)
        # Store session ID as a cookie
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
