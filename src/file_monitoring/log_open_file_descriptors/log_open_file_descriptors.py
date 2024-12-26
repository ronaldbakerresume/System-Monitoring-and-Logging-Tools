"""
Script: log_open_file_descriptors.py
Developer: Ronald Baker
Purpose: Detects and logs file descriptors opened by processes.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file

# Output file to save the log of open file descriptors
log_file = "open_file_descriptors_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Open File Descriptors Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        # Iterate through all running processes
        for process in psutil.process_iter(attrs=["pid", "name"]):
            try:
                # Get process details
                pid = process.info["pid"]
                name = process.info["name"]

                # Get the open file descriptors for the process
                open_files = process.open_files()

                # Log each open file descriptor
                if open_files:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = f"[{timestamp}] Process: PID {pid}, Name: {name}\n"
                    file.write(log_entry)
                    for f in open_files:
                        file.write(f"  Open File: {f.path}, Mode: {f.mode}\n")
                    file.write("\n")
                    print(f"Logged open file descriptors for PID {pid}, Name: {name}")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Skip processes that are inaccessible or have terminated
                continue

        print(f"Open file descriptors log saved to {log_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

