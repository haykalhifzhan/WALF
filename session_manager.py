#!/usr/bin/env python3
# WALF - Session Manager

import requests
from .config import HEADERS

def create_session():
    """Create and return a new requests session with default headers"""
    session = requests.Session()
    session.headers.update(HEADERS)
    return session
