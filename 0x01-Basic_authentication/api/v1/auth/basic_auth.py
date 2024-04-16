#!/usr/bin/env python3
"""Module that implements Basic authentication"""

from typing import TypeVar
from models.user import User
from base64 import b64decode
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentication management class"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts Base64 partof Authorization header for Basic Authentication
        Args:
            authorization_header (str): The Authorization header string
        Returns:
            str: Base64 part of Authorization header if valid,otherwise None"""
        if authorization_header and isinstance(
                authorization_header,
                str) and authorization_header.startswith('Basic '):
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes Base64 authorization header
        Args:
            base64_authorization_header (str)
        Return:
            decoded value as UTF-8 string if valid, otherwise None"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extracts the user email and password from the Base64 decoded value
        Args:
            decoded Base64 authorization header string
        Returns:
            Tuple[str, str]: email:password if valid, else (None, None)"""
        if not decoded_base64_authorization_header:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns the User instance based on the provided email and password
        Args:
            user_email (str): The email of the user
            user_pwd (str): The password of the user
        Returns:
            TypeVar('User'): The User instance if valid, otherwise None"""

        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        # Search for the user in the database
        user_list = User.search({'email': user_email})
        # If no user found with the provided email
        if not user_list:
            return None
        for user in user_list:
            if user.is_valid_password(user_pwd):
                return user
            else:
                return None
