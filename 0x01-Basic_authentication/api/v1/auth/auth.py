#!/usr/bin/env python3
"""Module that manages API authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Class that manages the client authentication process"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path"""
        return False

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user from the request"""
        return None
