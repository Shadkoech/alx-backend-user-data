#!/usr/bin/env python3
"""Module that manages API authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Class that manages the client authentication process"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path"""
        if path is None or not excluded_paths:
            return True
        for excluded_path in excluded_paths:
            if excluded_path in {path, path + '/'}:
                return False
            elif excluded_path.endswith('*') and path.startswith(
                excluded_path[:-1]):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user from the request"""
        return None
