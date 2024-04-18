#!/usr/bin/env python3
"""Module that implements session authentication"""

import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Class for session-based authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Method that creates session ID for user
        Args:
            user_id (str): User ID for which to create the session.
        Return:
            str: The generated Session ID"""

        if user_id is None or not isinstance(user_id, str):
            return None
        # Generate a Session ID
        session_id = str(uuid.uuid4())
        # Store the session ID with the corresponding user ID
        self.user_id_by_session_id[session_id] = user_id

        return session_id
