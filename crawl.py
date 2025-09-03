#!/usr/bin/env python3
# WALF - Crawl Module

import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .helpers import safe_get
from .utils import normalise_url, same_domain

def crawl_bfs(session, base_url, depth, logs=None):
    # Implementation remains the same as original
    # ... (code from original)
