"""
Script: log_excessive_file_descriptors.py
Developer: Ronald Baker
Purpose: Monitors and logs processes with excessive open file descriptors.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file

# Threshold for excessive open file descriptors
FILE_DESCRIPTOR_THRESHOLD = 100  # Example: More than 100 open files

# Output file to save the log of excessive file descriptor usage
log_file = "excessive_file_descriptors_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Excessive File Descriptors Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]

                    # Get the number of open file descriptors
                    num_fds = len(process.open_files())

                    # Check if the process exceeds the threshold
                    if num_fds > FILE_DESCRIPTOR_THRESHOLD:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Excessive File Descriptors Detected - "
                                     f"PID: {pid}, Name: {name}, Open File Descriptors: {num_fds}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Excessive file descriptors log saved.")

