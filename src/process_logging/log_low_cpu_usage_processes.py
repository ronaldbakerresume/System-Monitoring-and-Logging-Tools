"""
Script: log_low_cpu_usage_processes.py
Developer: Ronald Baker
Purpose: Monitors and logs processes with unusually low CPU usage over time to detect potential stalling or idle behavior.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Threshold for unusually low CPU usage (percentage)
LOW_CPU_USAGE_THRESHOLD = 1.0  # Example: Less than 1% CPU usage over the monitoring period

# Output file to save the log of low CPU usage processes
log_file = "low_cpu_usage_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Low CPU Usage Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name", "cpu_percent"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]
                    cpu_usage = process.info["cpu_percent"]

                    # Check if the CPU usage is below the threshold
                    if cpu_usage < LOW_CPU_USAGE_THRESHOLD:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Low CPU Usage Detected - "
                                     f"PID: {pid}, Name: {name}, CPU Usage: {cpu_usage:.2f}%\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Low CPU usage log saved.")

