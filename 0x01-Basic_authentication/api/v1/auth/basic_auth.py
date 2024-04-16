#!/usr/bin/env python3
"""Module that implements Basic authentication"""

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
