"""
Script: detect_runaway_processes.py
Developer: Ronald Baker
Purpose: Detects and logs runaway processes that exceed a predefined runtime duration.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime, timedelta  # For runtime calculations and timestamps
import time  # For periodic polling

# Threshold for runaway process runtime (in seconds)
RUNAWAY_RUNTIME_THRESHOLD = 3600  # 1 hour

# Output file to save the log of runaway processes
log_file = "runaway_processes_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Runaway Process Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
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

                    # Calculate the process runtime
                    runtime = datetime.now() - create_time

                    # Check if the process runtime exceeds the threshold
                    if runtime.total_seconds() > RUNAWAY_RUNTIME_THRESHOLD:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Runaway Process Detected - PID: {pid}, "
                                     f"Name: {name}, Runtime: {runtime.total_seconds():.2f} seconds\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Runaway process log saved.")

