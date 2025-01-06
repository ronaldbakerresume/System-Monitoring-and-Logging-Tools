"""
Script: log_stack_traces_high_resource_usage.py
Developer: Ronald Baker
Purpose: Captures and logs stack traces of processes consuming excessive resources (CPU or memory).
Compatible with: Linux, Windows, and Mac OS
"""

import os
import psutil  # For process monitoring
import traceback  # For formatting stack traces
from datetime import datetime  # To timestamp the log file

# Thresholds for high resource usage
CPU_THRESHOLD = 50.0  # Percentage of CPU usage
MEMORY_THRESHOLD_MB = 500  # Memory usage in MB

# Output file to save the log of high resource usage processes and their stack traces
log_file = "high_resource_usage_stack_traces_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"High Resource Usage Stack Trace Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        # Iterate through all running processes
        for process in psutil.process_iter(attrs=["pid", "name", "cpu_percent", "memory_info"]):
            try:
                # Get process details
                pid = process.info["pid"]
                name = process.info["name"]
                cpu_usage = process.info["cpu_percent"]
                memory_usage_mb = process.info["memory_info"].rss / (1024 * 1024)  # Convert to MB

                # Check if the process exceeds resource thresholds
                if cpu_usage > CPU_THRESHOLD or memory_usage_mb > MEMORY_THRESHOLD_MB:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = (f"[{timestamp}] High Resource Usage Process - PID: {pid}, "
                                 f"Name: {name}, CPU: {cpu_usage:.2f}%, "
                                 f"Memory: {memory_usage_mb:.2f} MB\n")
                    file.write(log_entry)
                    print(log_entry.strip())  # Print to the console

                    # Attempt to capture and log the process's stack trace
                    try:
                        stack_trace = "".join(traceback.format_stack())
                        stack_entry = f"Stack Trace for PID {pid}:\n{stack_trace}\n"
                        file.write(stack_entry)
                    except Exception as stack_error:
                        file.write(f"Error capturing stack trace for PID {pid}: {stack_error}\n")

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Skip processes that are inaccessible or have terminated
                continue

        print(f"High resource usage stack trace log saved to {log_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

