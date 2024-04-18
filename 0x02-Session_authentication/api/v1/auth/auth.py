#!/usr/bin/env python3
"""Module that manages API authentication"""

import os
from flask import request
from typing import List, TypeVar


class Auth:
    """Class that manages the client authentication process"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path"""
        if path is None or not excluded_paths:
            return True
        for ex_path in excluded_paths:
            if ex_path.endswith('*') and path.startswith(ex_path[:-1]):
                return False
            elif ex_path in {path, path + '/'}:
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

    def session_cookie(self, request=None):
        """Method that retrieves cookie value from a request
        Args:
            request: The request object
        Returns:
            str: Value of cookie named SESSION_NAME"""
        if request is None:
            return None

        # If SESSION_NAME is not found in environment variables,
        # the default value "_my_session_id" is used
        session_name = os.getenv("SESSION_NAME", "_my_session_id")
        return request.cookies.get(session_name)
