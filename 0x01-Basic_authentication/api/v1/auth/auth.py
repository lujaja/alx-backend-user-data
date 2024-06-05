#!/usr/bin/env python3
""" Class to manage API authentication"""
from flask import request
from typing import List, TypeVar
from models.user import import User 


class Auth():
    """ Define class Auth"""


    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Function require_auth"""
        return False
    
    def authorization_header(self, request=None) -> str:
        """ method authorized_header"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """ Method current_user"""
        return None
