#!/usr/bin/env python3
# WALF - ID Detection Module

from urllib.parse import urlparse, parse_qs
from .utils import normalise_url, detect_id_type
from .config import NUMERIC_RE

def detect_ids_in_url(u):
    # Implementation remains the same as original
    # ... (code from original)

def detect_ids_in_form(f):
    # Implementation remains the same as original
    # ... (code from original)

def gen_numeric(start, end): 
    return [str(i) for i in range(start, end+1)]

def gen_uuids(n): 
    return [str(uuid.uuid4()) for _ in range(n)]

def gen_base64_samples(n=3):
    # Implementation remains the same as original
    # ... (code from original)
