#!/usr/bin/env python3
""" Class BasicAuth"""
from api.v1.auth.auth import Auth
from typing import List
from api.v1.views import app_views
from flask import request
from flask.views import View, MethodView
from models.user import User


class BasicAuth(Auth):
    """ Class BasicAuth"""
    pass
