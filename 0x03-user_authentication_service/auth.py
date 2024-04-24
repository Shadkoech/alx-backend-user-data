#!/usr/bin/env python3
"""Module that hashes a password"""

import bcrypt


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
