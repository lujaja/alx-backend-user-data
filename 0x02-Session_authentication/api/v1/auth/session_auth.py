#!/usr/bin/env python3
""" Empty Session
"""
from api.v1.auth.auth import Auth
from typing import Dict
from uuid import uuid4


class SessionAuth(Auth):
    """ Define class SessionAuth"""
    user_id_by_session_id: Dict[str, str] = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creats a Session id for user_id"""
        if user_id is None or type(user_id) != str:
            return None
        self.user_id_by_session_id[str(uuid4())] = user_id
