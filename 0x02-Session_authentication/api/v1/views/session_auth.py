#!/usr/bin/env python3
""" Session Authentication views """
from flask import Blueprint, request, jsonify, abort
from models.user import User
from os import getenv

session_auth = Blueprint('session_auth', __name__)


@session_auth.route('/auth_session/login',
                    methods=['POST'], strict_slashes=False)
def login():
    """Login route"""
    from api.v1.app import auth  # Import here to avoid circular import issues

    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        user = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(getenv("SESSION_NAME"), session_id)

    return response


@session_auth.route('/auth_session/logout',
                    methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout route"""
    from api.v1.app import auth  # Import here to avoid circular import issues

    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
