#!/usr/bin/env python3
""" Class BasicAuth"""
from api.v1.auth.auth import Auth
from typing import List
from api.v1.views import app_views
from flask import request
from flask.views import View, MethodView
from models.user import User
import base64


class BasicAuth(Auth):
    """ Class BasicAuth
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
        self, base64_authorization_header: str
    ) -> str:
        """ Decode base64 authorization header """
        if (
            base64_authorization_header is None
            or type(base64_authorization_header) is not str
        ):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None
