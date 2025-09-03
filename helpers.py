#!/usr/bin/env python3
# WALF - Helpers Module

import requests
from bs4 import BeautifulSoup
from .config import TIMEOUT, HEADERS
from .utils import response_sig

def safe_get(session, url, **kwargs):
    try:
        return session.get(url, timeout=TIMEOUT, allow_redirects=True, **kwargs)
    except requests.RequestException as e:
        logger.debug(f"safe_get exception for {url}: {e}")
        return e

def safe_post(session, url, data=None, **kwargs):
    try:
        return session.post(url, data=data, timeout=TIMEOUT, allow_redirects=True, **kwargs)
    except requests.RequestException as e:
        logger.debug(f"safe_post exception for {url}: {e}")
        return e

def detect_id_type(val):
    # Implementation remains the same as original
    # ... (code from original)
