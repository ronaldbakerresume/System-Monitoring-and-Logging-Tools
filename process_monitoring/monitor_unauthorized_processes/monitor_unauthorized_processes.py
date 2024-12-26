
"""
Script: monitor_unauthorized_processes.py
Developer: Ronald Baker
Purpose: Monitors the system for unauthorized processes and logs their details.
Compatible with: Linux, Windows, and Mac OS
"""

import os
import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# List of authorized process names (case-sensitive)
AUTHORIZED_PROCESSES = [
    "python", "bash", "systemd", "explorer.exe", "chrome", "firefox"
]

# Output file to save the log of unauthorized processes
log_file = "unauthorized_processes_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Unauthorized Process Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name", "cmdline"]):
                try:
                    # Get process name and PID
                    process_name = process.info["name"]
                    process_cmd = " ".join(process.info["cmdline"])
                    process_pid = process.pid

                    # Check if the process is not authorized
                    if process_name not in AUTHORIZED_PROCESSES:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Unauthorized Process - PID: {process_pid}, "
                                     f"Name: {process_name}, Command: {process_cmd}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Unauthorized process log saved.")

