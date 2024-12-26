"""
Script: log_privilege_escalation_attempts.py
Developer: Ronald Baker
Purpose: Detects and logs unauthorized attempts to escalate privileges via processes.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# List of known privilege escalation commands or processes
ESCALATION_COMMANDS = ["sudo", "su", "setuid", "pkexec", "runas"]  # Example commands

# Output file to save the log of privilege escalation attempts
log_file = "privilege_escalation_attempts_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Privilege Escalation Attempts Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name", "cmdline", "username"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]
                    cmdline = " ".join(process.info.get("cmdline", []))
                    username = process.info.get("username", "N/A")

                    # Check if the command line contains any known escalation command
                    if any(cmd in cmdline for cmd in ESCALATION_COMMANDS):
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Privilege Escalation Detected - PID: {pid}, "
                                     f"Name: {name}, User: {username}, Command: {cmdline}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Privilege escalation attempts log saved.")

