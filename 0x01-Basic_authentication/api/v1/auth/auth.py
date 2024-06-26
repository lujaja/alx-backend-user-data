#!/usr/bin/env python3
""" Class to manage API authentication"""

from flask import request
from typing import List, TypeVar
import re

User = TypeVar('User')


class Auth():
    """ Define class Auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Function require_auth"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for ex_path in excluded_paths:
            ex_path = ex_path.replace('*', '*')
            if re.match(ex_path, path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ method authorized_header"""
        try:
            return request.headers['Authorization']
        except Exception:
            return None

    def current_user(self, request=None) -> User:
        """ Current_user"""
        return None
