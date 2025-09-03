#!/usr/bin/env python3
# WALF - Configuration Module

import os
import re

# ----------------- CONFIG -----------------
TIMEOUT = 8
THROTTLE = 0.6
CRAWL_DEPTH = 1
ID_NUM_RANGE_DEFAULT = (1, 5)
UUID_SAMPLE_COUNT = 3
HEADERS = {"User-Agent": "WALF/1.0 (Level-3)"}
REPORT_DIR = "reports"
LOG_FILE = "walf_scan.log"

COMMON_LOGIN_PATHS = ["/login", "/signin", "/users/sign_in", "/auth/login", "/accounts/login", "/signin.php"]
ADMIN_PATHS = ["/admin", "/administrator", "/admin/dashboard", "/manage"]

# Regex patterns
UUID_RE = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
NUMERIC_RE = re.compile(r"^\d+$")
BASE64_RE = re.compile(r"^[A-Za-z0-9+/=]{8,}$")
MD5_RE = re.compile(r"^[a-fA-F0-9]{32}$")
SHA1_RE = re.compile(r"^[a-fA-F0-9]{40}$")
SHA256_RE = re.compile(r"^[a-fA-F0-9]{64}$")

# PII regex (for redaction)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"\+?\d[\d\-\s]{6,}\d")

# Common paths for testing
COMMON_ADMIN_PATHS = ADMIN_PATHS + ["/admin/login","/admin-console","/manage/account","/cms","/dashboard/admin","/admin/api","/api/admin"]
COMMON_GUESS_SUFFIXES = ["/orders/{}","/order/{}","/invoices/{}","/transactions/{}"]
