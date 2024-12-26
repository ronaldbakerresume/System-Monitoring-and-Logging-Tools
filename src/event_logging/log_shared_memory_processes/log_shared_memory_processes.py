"""
Script: log_shared_memory_processes.py
Developer: Ronald Baker
Purpose: Tracks processes using shared memory and logs their details.
Compatible with: Linux, Windows, and Mac OS
"""

import os
import psutil  # For system process monitoring
from datetime import datetime  # To timestamp the log file

# Output file to save the log of processes using shared memory
log_file = "shared_memory_processes_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Shared Memory Process Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        # Iterate through all running processes
        for process in psutil.process_iter(attrs=["pid", "name", "memory_info"]):
            try:
                # Get process details
                pid = process.info["pid"]
                name = process.info["name"]
                memory_info = process.info["memory_info"]

                # Check if shared memory usage is present
                if hasattr(memory_info, "shared"):
                    shared_memory = memory_info.shared
                    if shared_memory > 0:  # Log processes with non-zero shared memory
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Process: PID {pid}, Name: {name}, "
                                     f"Shared Memory: {shared_memory / (1024 * 1024):.2f} MB\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Skip processes that are inaccessible or have terminated
                continue

        print(f"Shared memory usage log saved to {log_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

