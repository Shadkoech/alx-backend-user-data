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
