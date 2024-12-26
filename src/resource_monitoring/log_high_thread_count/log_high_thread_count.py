"""
Script: log_high_thread_count.py
Developer: Ronald Baker
Purpose: Monitors and logs processes with high thread counts to identify potential thread overuse.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Threshold for high thread count
THREAD_COUNT_THRESHOLD = 100  # Example: More than 100 threads

# Output file to save the log of high thread count processes
log_file = "high_thread_count_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"High Thread Count Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name", "num_threads"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]
                    thread_count = process.info["num_threads"]

                    # Check if the thread count exceeds the threshold
                    if thread_count > THREAD_COUNT_THRESHOLD:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] High Thread Count Detected - "
                                     f"PID: {pid}, Name: {name}, Thread Count: {thread_count}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. High thread count log saved.")

