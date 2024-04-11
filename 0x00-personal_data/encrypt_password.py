#!/usr/bin/env python3
"""Module that encrypts password using bycrypt package"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Method that hashes a password using bcrypt with salt
    Args:
        password: Password to be hashed
    Returns:
        bytes: Salted, hashed password"""

    # Generate a salt for hashing
    salt = bcrypt.gensalt()
    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks is a password matches the hashed password
    Args:
        hashed_password (bytes): The hashed password
        password (str): The password to check
    Returns:
        bool: True if password matches hashed password, False otherwise"""
    # use bcrypt.checkpw() to validate whether provided \
    # plain text password matches the hashed password.
    # encode() method is used to convert a string to its corresponding bytes

    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
