#!/usr/bin/env python3
# WALF - Utilities Module

import os
import time
import uuid
import base64
import csv
import html
from difflib import SequenceMatcher
from urllib.parse import urljoin, urlparse, parse_qs, urlencode, urlunparse
from .config import EMAIL_RE, PHONE_RE, REPORT_DIR

# ----------------- UTIL (scan id, finding helpers) -----------------
def gen_scan_id():
    return time.strftime("walf-%Y%m%d-%H%M%S", time.localtime())

def gen_finding_id(scan_id, seq=1):
    return f"{scan_id}-F-{seq:04d}"

def assess_severity(f):
    """Heuristic scoring -> severity + numeric score"""
    # Implementation remains the same as original
    # ... (code from original)

def build_poc_curl(f, session_cookie_name="session"):
    """Build a quick PoC curl string. Replace cookie placeholder before use."""
    # Implementation remains the same as original
    # ... (code from original)

def dedupe_findings(findings):
    # Implementation remains the same as original
    # ... (code from original)

def redact_text(s):
    # Implementation remains the same as original
    # ... (code from original)

def ensure_reports_dir():
    try:
        os.makedirs(REPORT_DIR, exist_ok=True)
    except Exception as e:
        logger.debug(f"ensure_reports_dir error: {e}")

def export_csv(findings, fname):
    # Implementation remains the same as original
    # ... (code from original)

def normalise_url(u):
    # Implementation remains the same as original
    # ... (code from original)

def same_domain(a, b):
    # Implementation remains the same as original
    # ... (code from original)

def similarity(a, b):
    # Implementation remains the same as original
    # ... (code from original)

def response_sig(resp):
    # Implementation remains the same as original
    # ... (code from original)

def login_success_heuristic(resp):
    # Implementation remains the same as original
    # ... (code from original)

def _short(text, n=800):
    # Implementation remains the same as original
    # ... (code from original)

def try_parse_json(text):
    # Implementation remains the same as original
    # ... (code from original)

def normalize_json(obj):
    # Implementation remains the same as original
    # ... (code from original)
