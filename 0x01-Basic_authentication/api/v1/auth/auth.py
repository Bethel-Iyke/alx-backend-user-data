#!/usr/bin/env python3
"""Creates the class Auth that has different methods"""

from flask import request
from typing import List, TypeVar


class Auth():
    """Manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return a boolean."""
        if not path or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path\
                    or path.startswith(excluded_path + '/')\
                    or (excluded_path.endswith('/')
                        and path.startswith(excluded_path[:-1])):
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
