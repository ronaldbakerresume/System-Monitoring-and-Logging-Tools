"""
Script: monitor_command_line_arguments.py
Developer: Ronald Baker
Purpose: Monitors command-line arguments of running processes and logs suspicious activity based on predefined patterns.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For system process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Predefined list of suspicious keywords in command-line arguments
SUSPICIOUS_KEYWORDS = ["hack", "exploit", "malware", "ransomware", "unauthorized"]

# Output file to save the log of suspicious activity
log_file = "suspicious_command_args_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Suspicious Command-Line Arguments Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name", "cmdline"]):
                try:
                    # Extract command-line arguments
                    cmdline = process.info.get("cmdline", [])

                    # Check if any keyword from the suspicious list is present
                    if any(keyword in " ".join(cmdline).lower() for keyword in SUSPICIOUS_KEYWORDS):
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Suspicious Process Detected - PID: {process.pid}, "
                                     f"Name: {process.info['name']}, Command: {' '.join(cmdline)}\n")

                        # Log the suspicious activity
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Suspicious command-line arguments log saved.")

