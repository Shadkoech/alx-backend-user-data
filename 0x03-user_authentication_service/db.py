#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Methid adding a user into the db
        Args:
            email (str): The email of the user
            hashed_password (str): hashed password of the user
        Returns:
            User: The newly added User object"""

        try:
            new_user = User(email=email, hashed_password=hashed_password)
            # Add the new_user object to the session
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            # Rollback the transaction in case of an error
            self._session.rollback()
            new_user = None
        return new_user
