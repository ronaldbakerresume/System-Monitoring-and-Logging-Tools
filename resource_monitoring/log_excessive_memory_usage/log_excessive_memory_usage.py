"""
Script: log_excessive_memory_usage.py
Developer: Ronald Baker
Purpose: Monitors and logs processes consuming excessive memory over time.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Threshold for excessive memory usage (in MB)
MEMORY_USAGE_THRESHOLD_MB = 500  # Example: 500 MB

# Output file to save the log of excessive memory usage
log_file = "excessive_memory_usage_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Excessive Memory Usage Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name", "memory_info"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]
                    memory_usage = process.info["memory_info"].rss / (1024 * 1024)  # Convert bytes to MB

                    # Check if the memory usage exceeds the threshold
                    if memory_usage > MEMORY_USAGE_THRESHOLD_MB:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Excessive Memory Usage Detected - "
                                     f"PID: {pid}, Name: {name}, Memory Usage: {memory_usage:.2f} MB\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Excessive memory usage log saved.")

