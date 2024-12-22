"""
Script: log_temp_file_disk_usage.py
Developer: Ronald Baker
Purpose: Monitors and logs disk space usage of processes writing to temporary files.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process and file monitoring
from datetime import datetime  # To timestamp the log file
import os
import time  # For periodic polling

# Path to the temporary directory
TEMP_DIR = "/tmp" if os.name != "nt" else "C:\\Windows\\Temp"

# Output file to save the log of disk space usage
log_file = "temp_file_disk_usage_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Temporary File Disk Usage Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]

                    # Check open files of the process
                    temp_file_usage = 0
                    for f in process.open_files():
                        if f.path.startswith(TEMP_DIR):
                            temp_file_usage += os.path.getsize(f.path)

                    # Log processes with non-zero temporary file disk usage
                    if temp_file_usage > 0:
                        temp_usage_mb = temp_file_usage / (1024 * 1024)  # Convert bytes to MB
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Process: PID {pid}, Name: {name}, "
                                     f"Temporary Disk Usage: {temp_usage_mb:.2f} MB\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied, FileNotFoundError):
                    # Skip processes that are inaccessible or files that are removed
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Temporary file disk usage log saved.")

