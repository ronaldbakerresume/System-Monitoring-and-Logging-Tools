"""
Script: log_critical_directory_access.py
Developer: Ronald Baker
Purpose: Monitors processes accessing critical directories (e.g., /etc, /home) and logs their details.
Compatible with: Linux, Windows, and Mac OS
"""

import os
import psutil  # For process and file monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# List of critical directories to monitor
CRITICAL_DIRECTORIES = ["/etc", "/home", "C:\\Windows\\System32", "/var"]

# Output file to save the log of processes accessing critical directories
log_file = "critical_directory_access_log.txt"

# Function to check if a process accesses critical directories
def is_accessing_critical_directory(proc):
    """
    Checks if a process has opened files in critical directories.
    """
    try:
        # Iterate through all open files of the process
        for file in proc.open_files():
            # Check if the file path starts with any critical directory
            for directory in CRITICAL_DIRECTORIES:
                if file.path.startswith(directory):
                    return True, file.path
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Skip processes that are inaccessible or have terminated
        pass
    return False, None

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Critical Directory Access Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name"]):
                try:
                    # Check if the process accesses critical directories
                    accessing, path = is_accessing_critical_directory(process)
                    if accessing:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Process: PID {process.info['pid']}, "
                                     f"Name: {process.info['name']}, Accessed Path: {path}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Critical directory access log saved.")

