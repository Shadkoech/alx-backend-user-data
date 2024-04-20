#!/usr/bin/env python3
"""Model to facilitate thestorage of sessions in a database"""

from models.base import Base


class UserSession(Base):
    """User session class that inherits from Base"""

    def __init__(self, *args: list, **kwargs: dict):
        """Initialize UserSession instance
        Args:
            user_id (str): The ID of the user
            session_id (str): The session ID"""

        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
