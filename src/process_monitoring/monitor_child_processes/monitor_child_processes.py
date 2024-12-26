"""
Script: monitor_child_processes.py
Developer: Ronald Baker
Purpose: Monitors child processes spawned by a specific parent process and logs their details.
Compatible with: Linux, Windows, and Mac OS
"""

import os
import psutil  # For process management
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Specify the PID of the parent process to monitor
parent_pid = 1234  # Replace with the PID of the parent process you want to monitor

# Output file to save the log of child processes
log_file = "child_processes_log.txt"

# Function to monitor child processes
def monitor_child_processes(pid):
    """
    Monitors child processes spawned by the specified parent PID.
    """
    try:
        parent = psutil.Process(pid)  # Get the parent process object
        children = parent.children(recursive=True)  # Get all child processes
        return children
    except psutil.NoSuchProcess:
        return []  # Return an empty list if the parent process no longer exists

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Child Process Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        # Track previously logged child PIDs to avoid duplicate logs
        logged_pids = set()

        while True:
            # Get the current list of child processes
            child_processes = monitor_child_processes(parent_pid)

            # Log details of new child processes
            for child in child_processes:
                if child.pid not in logged_pids:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = (f"[{timestamp}] Child PID: {child.pid}, Name: {child.name()}, "
                                 f"Command: {' '.join(child.cmdline())}\n")
                    file.write(log_entry)
                    print(log_entry.strip())  # Print to console as well
                    logged_pids.add(child.pid)  # Add the PID to the logged set

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Child process log saved.")

