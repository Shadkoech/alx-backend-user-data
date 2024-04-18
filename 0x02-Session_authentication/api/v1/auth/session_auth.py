#!/usr/bin/env python3
"""Module that implements session authentication"""

import uuid
from models.user import User
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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Method retrieving User ID based on a Session ID
        Args:
            session_id (str): Session ID for which to retrieve the User ID
        Returns:
            str: User ID associated with the Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None

        # Retrieve the User ID for the given Session ID
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Method returning user instance based on cookie value
        Args:
            request: The request object
        Returns:
        User: The current user instance"""
        # Retrieve the session cookie value
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)

        return user

    def destroy_session(self, request=None):
        """Delete the user session / logout
        Args:
            request: The request object.
        Returns:
            bool: True if session was successfully destroyed, False otherwise.
        """
        if not request:
            return False

        # Retrieve the session ID from the request cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        # Check if the session ID is linked to any user ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        # If session ID is linked to user ID,
        # delete the session ID from the dictionary
        del self.user_id_by_session_id[session_id]
        return True
