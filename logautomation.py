#!/usr/bin/env python3

import re
import subprocess
from datetime import datetime

# ===== Timestamped output file =====
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
SUMMARY_FILE = f"/home/hexis/python/log_summary_{timestamp}.txt"

# ===== Regex patterns for detecting log events =====
ERROR_PATTERN = re.compile(r"\berror\b", re.IGNORECASE)
WARNING_PATTERN = re.compile(r"\bwarn(ing)?\b", re.IGNORECASE)
FAILED_PATTERN = re.compile(r"\bfail(ed)?\b", re.IGNORECASE)

def analyze_logs():
    print("[🧠] Fetching system logs using journalctl...")

    # Fetch last 500 log entries
    logs = subprocess.run(["journalctl", "-n", "500"], capture_output=True, text=True)

    if logs.returncode != 0:
        print("⚠️  Failed to fetch logs!")
        return

    error_count = 0
    warning_count = 0
    failed_count = 0
    recent_logs = []

    # ===== Process each log line =====
    for line in logs.stdout.splitlines():
        if ERROR_PATTERN.search(line):
            error_count += 1
        if WARNING_PATTERN.search(line):
            warning_count += 1
        if FAILED_PATTERN.search(line):
            failed_count += 1

        recent_logs.append(line.strip())

    # ===== Prepare summary =====
    summary = f"""
===============================
🧩 System Log Analysis Report
📅 {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
===============================

Total Lines Analyzed: {len(recent_logs)}

🚨 Errors: {error_count}
⚠️  Warnings: {warning_count}
❌ Failed Events: {failed_count}

Recent Entries:
----------------
{chr(10).join(recent_logs[-10:])}
----------------

Report saved at: {SUMMARY_FILE}
"""

    # ===== Write to file =====
    with open(SUMMARY_FILE, "w") as f:
        f.write(summary)

    print(summary)

if __name__ == "__main__":
    analyze_logs()
