#!/usr/bin/env python3
""" Empty Session
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """ Define class SessionAuth"""
    user_id_by_session_id: dict = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creats a Session id for user_id"""
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ User ID for Session ID"""
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Use Session ID for identifying a user"""
        session_id = self.session_cookie(request)
        if session_id:
            user_id = self.user_id_by_session_id.get(session_id)
            if user_id is None:
                return None
            return User.get(user_id)
        return None
