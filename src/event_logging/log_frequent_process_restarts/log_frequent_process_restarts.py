"""
Script: log_frequent_process_restarts.py
Developer: Ronald Baker
Purpose: Detects and logs processes that restart frequently within a specified time window.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime, timedelta  # For timestamp calculations and logging
import time  # For periodic polling

# Threshold for frequent restarts (number of restarts within the time window)
RESTART_THRESHOLD = 3  # Example: 3 restarts
# Time window for monitoring restarts (in seconds)
TIME_WINDOW = 60  # Example: 60 seconds

# Output file to save the log of frequent restarts
log_file = "frequent_process_restarts_log.txt"

# Dictionary to track process restarts (PID -> [start_times])
restart_tracker = {}

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Frequent Process Restarts Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name", "create_time"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]
                    create_time = datetime.fromtimestamp(process.info["create_time"])

                    # Track process restarts
                    if pid not in restart_tracker:
                        restart_tracker[pid] = [create_time]
                    else:
                        # Add the latest start time
                        restart_tracker[pid].append(create_time)

                        # Remove old start times outside the monitoring time window
                        restart_tracker[pid] = [
                            t for t in restart_tracker[pid] if (datetime.now() - t).total_seconds() <= TIME_WINDOW
                        ]

                        # Check if the restart count exceeds the threshold
                        if len(restart_tracker[pid]) > RESTART_THRESHOLD:
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            log_entry = (f"[{timestamp}] Frequent Restarts Detected - PID: {pid}, "
                                         f"Name: {name}, Restarts: {len(restart_tracker[pid])}\n")
                            file.write(log_entry)
                            print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Frequent process restart log saved.")

