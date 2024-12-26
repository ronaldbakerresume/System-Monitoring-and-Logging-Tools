"""
Script: log_file_locking_processes.py
Developer: Ronald Baker
Purpose: Monitors and logs processes holding locks on specific files.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process and file monitoring
from datetime import datetime  # To timestamp the log file

# List of specific files to monitor for locks
MONITORED_FILES = ["/etc/passwd", "/var/log/syslog", "C:\\Windows\\System32\\config\\SAM"]

# Output file to save the log of file-locking processes
log_file = "file_locking_processes_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"File Locking Processes Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name"]):
                try:
                    # Check open files for the process
                    for f in process.open_files():
                        # Check if the file path matches any monitored file
                        if f.path in MONITORED_FILES:
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            log_entry = (f"[{timestamp}] File Lock Detected - "
                                         f"PID: {process.info['pid']}, Name: {process.info['name']}, "
                                         f"File: {f.path}\n")
                            file.write(log_entry)
                            print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. File locking log saved.")
