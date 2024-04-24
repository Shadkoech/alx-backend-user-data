#!/usr/bin/env python3
"""Module that hashes a password"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Method generating salted hash of the input password
    Args:
        Password: The password string to hash
    Returns:
        bytes: salted hash of the input password"""
    # Convert the password string to bytes
    password_bytes = password.encode('utf-8')

    # Generate salted hash of passwd using bcrypt
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method registering new user
        Args:
            email (str): The email of the user
            password (str): The password of the user"""

        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)

            return new_user
