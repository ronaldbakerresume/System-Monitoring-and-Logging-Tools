"""
Script: monitor_virtual_memory_usage.py
Developer: Ronald Baker
Purpose: Monitors processes consuming significant virtual memory and logs their details.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Threshold for significant virtual memory usage (in MB)
VIRTUAL_MEMORY_THRESHOLD_MB = 500  # Example: 500 MB

# Output file to save the log of processes with high virtual memory usage
log_file = "high_virtual_memory_processes_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"High Virtual Memory Usage Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name", "memory_info"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]
                    memory_info = process.info["memory_info"]

                    # Check virtual memory usage (vms is the virtual memory size in bytes)
                    virtual_memory_mb = memory_info.vms / (1024 * 1024)  # Convert to MB

                    if virtual_memory_mb > VIRTUAL_MEMORY_THRESHOLD_MB:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Process: PID {pid}, Name: {name}, "
                                     f"Virtual Memory: {virtual_memory_mb:.2f} MB\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. High virtual memory usage log saved.")

