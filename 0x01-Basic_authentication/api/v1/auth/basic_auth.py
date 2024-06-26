#!/usr/bin/env python3
""" Module Basic_auth for user authentication
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """ Extends BasicAuth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Method extract_base64_authorization_header
        """

        if (
            authorization_header is None
            or type(authorization_header) is not str
            or not authorization_header.startswith('Basic ')
        ):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, aut_header: str) -> str:
        """ Decode base64 authorization header """
        if (
            aut_header is None
            or type(aut_header) is not str
        ):
            return None
        try:
            decoded_bytes = base64.b64decode(aut_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, header: str) -> (str, str):
        """ Method extract_user_credentials """
        if (
            header is None
            or type(header) is not str
            or ':' not in header
        ):
            return None, None
        email, psswd = header.split(':', 1)
        return email, psswd

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Return the User instance based on email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        user = User.search({"email": user_email})
        if user is None or len(user) == 0:
            return None

        user = user[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current_user"""
        if request is None:
            return None
        auth = self.authorization_header(request)
        if auth is None:
            return None
        base64_auth = self.extract_base64_authorization_header(auth)
        if base64_auth is None:
            return None
        decoded_base64_auth = self.decode_base64_authorization_header(
            base64_auth
        )
        if decoded_base64_auth is None:
            return None
        email, pwd = self.extract_user_credentials(decoded_base64_auth)
        if email is None or pwd is None:
            return None
        user = self.user_object_from_credentials(email, pwd)
        return user
