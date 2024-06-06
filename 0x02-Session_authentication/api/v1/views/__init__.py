#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import all view modules
from api.v1.views.index import *
from api.v1.views.users import *

# Register the blueprint for session_auth
# app_views.register_blueprint(session_auth)

# Load User data
User.load_from_file()
