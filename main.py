#!/usr/bin/env python3
# WALF - Main Entry Point (Modular Version)

import os
import time
import getpass
from urllib.parse import urlparse

# Import modules
from walf.config import *
from walf.logger import setup_logger
from walf.utils import gen_scan_id, normalise_url, validate_target_url
from walf.helpers import safe_get, safe_post
from walf.login import detect_login_candidates, inspect_form_html, dump_login_debug, verify_session_auth
from walf.crawl import crawl_bfs
from walf.id_detection import detect_ids_in_url, detect_ids_in_form
from walf.scenarios import *
from walf.report import finalize_and_export, render_html_report
from walf.session_manager import create_session

# Setup logger
logger = setup_logger()

# ----------------- CLI BANNER -----------------
def print_banner(scan_id):
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║              WALF - Web Access Logic Framework           ║")
    print("║   Advanced IDOR & Privilege Escalation Testing Tool      ║")
    print("╚══════════════════════════════════════════════════════════╝\n")
    print(f"[+] Scan ID: {scan_id}")
    print("[+] Mode: Full Flow (Login → Crawl → Access Logic Scenarios)")
    print("[+] Description: Automated framework to detect IDOR & PrivEsc")
    print("----------------------------------------------------------------\n")

# ----------------- MAIN FLOW -----------------
def main():
    try:
        SCAN_ID = gen_scan_id()
        print_banner(SCAN_ID)
        
        # Get target URL
        target = input("⚡ Target URL (contoh: http://127.0.0.1:5002): ").strip()
        try:
            target = validate_target_url(target)
        except Exception as ve:
            print(f"Input URL tidak valid: {ve}")
            return

        # Get report name
        report_base_name = input("Masukkan nama dasar untuk file laporan (contoh: report_website): ").strip()
        if not report_base_name:
            try:
                domain_name = urlparse(target).netloc.replace('.', '_').replace(':', '_')
                report_base_name = f"{domain_name}"
            except:
                report_base_name = "idor_report"
            print(f"Nama dasar tidak diisi, menggunakan default: '{report_base_name}'")

        # Initialize output structure
        output = {
            "url": target, 
            "login_detected_paths": [], 
            "auth_type_candidates": [], 
            "login_path_used": None, 
            "auth_type_used": None, 
            "login_success": False, 
            "found_urls": [], 
            "found_forms": [], 
            "found_ids": [], 
            "findings": [], 
            "errors": [], 
            "recommendations": [], 
            "logs": [], 
            "meta": {"timeout": TIMEOUT, "throttle": THROTTLE, "crawl_depth": CRAWL_DEPTH}
        }

        # Create session
        session = create_session()

        # 1) Detect login
        try:
            candidates = detect_login_candidates(target, session, output["logs"])
            # ... (rest of the main flow remains similar but with modular imports)
            
        except Exception as e:
            output["errors"].append(f"Error detecting login: {e}")
            output["logs"].append({"ts": time.time(), "level": "error", "msg": str(e)})

        # ... (rest of the main function)

        # Finalize and export
        final, html_file, json_file, csv_file = finalize_and_export(output, report_base_name, SCAN_ID)

        print("\n✔ Testing complete!")
        print(f"📄 Reports saved:\n  - HTML: {html_file}\n  - JSON: {json_file}\n  - CSV:  {csv_file}")
        print("\nSelesai. Ingat: jangan menyimpan kredensial di file; tool ini tidak menyimpan kredensial ke output.")
        
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")
    except Exception as e:
        logger.exception(f"Fatal error in main: {e}")
        print(f"[-] Fatal error: {e}")

if __name__ == "__main__":
    main()
