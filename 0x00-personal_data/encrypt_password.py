#!/usr/bin/env python3
"""
Encrypt password
"""
from bcrypt import hashpw, checkpw, gensalt


def hash_password(password: str) -> bytes:
    """ Hash password """
    return hashpw(password.encode('utf-8'), gensalt())


def is_valid(hashed_password, password):
    """ Validate password """
    return checkpw(password.encode('utf-8'), hashed_password)
