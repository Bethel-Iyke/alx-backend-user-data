#!/usr/bin/env python3
"""Creates the class Auth that has different methods"""

from flask import request
from typing import List, TypeVar

class Auth():
    """the class auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """the method require auth"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            if path.rstrip('/').startswith(excluded_path.rstrip('/')):
                return False
            return True

    def authorization_header(self, request=None) -> str:
        """the method authorization header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """the  method current user"""
        return None
