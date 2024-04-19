#!/usr/bin/env python3
"""Module that sets expiration to authentication sessions"""

from os import getenv
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Class for session-based authentication with session expiration"""

    def __init__(self):
        """Initialize the SessionExpAuth instance"""

        super().__init__()
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create a session with expiration
        Args:
            user_id (str): The ID of the user
        Returns:
            str: The created session ID."""

        # Call the create_session method of the parent class
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        # Create session dictionary with user_id and created_at
        session_dict = {
            "user_id": user_id,
            "created_at": datetime.now()
        }

        # Store session dictionary in user_id_by_session_id using \
        # session_id as key
        self.user_id_by_session_id[session_id] = session_dict

        return session_id

    def user_id_for_session_id(self, session_id=None) -> str:
        """Retrieve user ID based on session ID with expiration
        Args:
            session_id (str): The session ID
        Returns:
            str: User ID if session is valid and not expired, None otherwise"""

        if session_id is None or isinstance(session_id, str) is False:
            return None
        # Retrieve session dictionary for given session_id
        session_dict = self.user_id_by_session_id.get(session_id)

        if session_dict is None or 'created_at' not in session_dict:
            return None

        # Check if session duration is set and valid
        if self.session_duration <= 0:
            return session_dict.get("user_id")

        # Check if session has expired
        created_time = session_dict.get('created_at')
        session_elapsed = timedelta(seconds=self.session_duration)

        if created_time + session_elapsed < datetime.now():
            return None
        else:
            return session_dict.get('user_id')
