"""
Script: log_priority_changes.py
Developer: Ronald Baker
Purpose: Tracks and logs scheduling priority changes for running processes.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Output file to save the log of priority changes
log_file = "priority_changes_log.txt"

# Dictionary to track the last known priority of each process
process_priorities = {}

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Process Priority Changes Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name", "nice"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]
                    current_priority = process.info["nice"]  # Nice value represents priority

                    # Check for priority changes
                    if pid in process_priorities and process_priorities[pid] != current_priority:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Priority Change Detected - PID: {pid}, "
                                     f"Name: {name}, Old Priority: {process_priorities[pid]}, "
                                     f"New Priority: {current_priority}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                    # Update the priority in the tracking dictionary
                    process_priorities[pid] = current_priority

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    if pid in process_priorities:
                        del process_priorities[pid]  # Remove terminated processes from tracking
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Priority changes log saved.")

