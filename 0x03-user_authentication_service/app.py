#!/usr/bin/env python3
"""Module that sets up a flask app"""

from auth import Auth
from flask import Flask, jsonify, request

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
