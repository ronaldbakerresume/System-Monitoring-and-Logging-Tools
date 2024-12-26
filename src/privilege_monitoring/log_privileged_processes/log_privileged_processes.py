"""
Script: log_privileged_processes.py
Developer: Ronald Baker
Purpose: Monitors and logs processes running with root or administrator privileges.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import os  # For platform-specific privilege checks

# Output file to save the log of privileged processes
log_file = "privileged_processes_log.txt"

# Function to check if a process is running with elevated privileges
def is_privileged(process):
    """
    Determines if the process is running with elevated privileges.
    """
    try:
        if os.name == "nt":  # Windows-specific check for administrator privileges
            return process.username() == "NT AUTHORITY\\SYSTEM"
        else:  # Unix-based check for root privileges
            return process.username() == "root"
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return False

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Privileged Processes Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name", "username"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]

                    # Check if the process is running with elevated privileges
                    if is_privileged(process):
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Privileged Process Detected - "
                                     f"PID: {pid}, Name: {name}, User: {process.info['username']}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Privileged processes log saved.")

