# 🧠 Automated Log Analyzer (Python + Cron)

## 📜 Overview

The **Automated Log Analyzer** is a Python-based system monitoring tool that automatically fetches and analyzes system logs using `journalctl`.  
It detects and summarizes **errors**, **warnings**, and **failed events** — then stores them as timestamped reports.  
The script can be scheduled with **cron jobs** to run automatically at specific time intervals.

---

## 🧩 Features

- 🔍 **Log Fetching:** Collects the latest 500 logs from `journalctl`.  
- ⚙️ **Regex Analysis:** Detects key terms like `error`, `warning`, and `failed`.  
- 📊 **Summary Reports:** Creates readable summaries with counts and recent log entries.  
- 🕒 **Timestamped Output:** Each run generates a unique report file with a timestamp.  
- 🤖 **Automation:** Can be scheduled via **cron** for unattended execution.

---

## 🧠 Tech Stack

| Component | Description |
|------------|-------------|
| **Python 3** | Core programming language |
| **Regex (`re`)** | For detecting log patterns |
| **Subprocess** | Runs Linux commands like `journalctl` |
| **Cron** | Automates periodic execution |
| **Linux System Logs** | Data source for analysis |

---

## 🧰 Prerequisites

Before running the project, ensure you have:

- 🐧 Linux system (with `systemd` and `journalctl`)  
- 🐍 Python 3 installed  
- Access to create cron jobs (`crontab -e`)  
- A directory for reports, e.g., `/home/hexis/python/`

---

### How to set up this script in cron

1. Make sure your Python script is executable:
   chmod +x /home/hexis/python/log_analyzer.py

2. Find the path of your Python interpreter:
   which python3
   (usually it’s /usr/bin/python3)

3. Open your crontab editor:
   crontab -e

4. Add this line at the end of the file:
   */5 * * * * /usr/bin/python3 /home/hexis/python/log_analyzer.py >> /home/hexis/Scripts/sysmon_cron.log 2>&1

   EXPLANATION:
   - */5  means every 5 minutes
   - *    means every hour/day/month (default)
   - /usr/bin/python3  is the Python interpreter
   - /home/hexis/python/log_analyzer.py  is your script path
   - >> appends output (standard + error) to sysmon_cron.log
   - 2>&1 merges errors (2) into normal output (1)

5. Save and exit the editor.
   (In nano: press CTRL + O to save, then CTRL + X to exit)

6. Verify that the cron job was added:
   crontab -l

   You should see:
   */5 * * * * /usr/bin/python3 /home/hexis/python/log_analyzer.py >> /home/hexis/Scripts/sysmon_cron.log 2>&1

7. Optional: check cron logs to make sure it runs:
   grep CRON /var/log/syslog  (on Ubuntu/Debian)
   or
   journalctl -u cron.service  (on Fedora)

8. After 5 minutes, check your output files:
   ls /home/hexis/python/log_summary_*.txt

   You should see new timestamped reports being created automatically.


