#!/usr/bin/env python3
"""Module that hashes a password"""

import uuid
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


def _generate_uuid():
    """GGenerates new UUID and returns as a string rep
    Returns:
        str: string representation of new UUID"""
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Method checking if login credentials are valid
        Args:
            email (str): The email of the user
            password (str): The password of the user"""

        try:
            user = self._db.find_user_by(email=email)

            # Check if the provided password matches the hashed password
            hashed_password = user.hashed_password
            provided_password = password.encode('utf-8')
            if bcrypt.checkpw(provided_password, hashed_password):
                return True
            else:
                return False

        except NoResultFound:
            # If no user found with the email, return False
            return False

    def create_session(self, email: str) -> str:
        """method creating session for a user based on given email
        Args:
            email (str): The email address of the user
        Returns:
            str: The session ID generated for the user"""

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id
