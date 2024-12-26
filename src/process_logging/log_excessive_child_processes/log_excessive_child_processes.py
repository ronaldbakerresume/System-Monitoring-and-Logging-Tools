"""
Script: log_excessive_child_processes.py
Developer: Ronald Baker
Purpose: Monitors and logs processes spawning excessive child processes to detect potential process spawning loops or abuse.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Threshold for excessive child processes
CHILD_PROCESS_THRESHOLD = 10  # Example: More than 10 child processes

# Output file to save the log of excessive child processes
log_file = "excessive_child_processes_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Excessive Child Processes Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]

                    # Get the child processes of the current process
                    child_processes = process.children(recursive=True)

                    # Check if the number of child processes exceeds the threshold
                    if len(child_processes) > CHILD_PROCESS_THRESHOLD:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Excessive Child Processes Detected - "
                                     f"PID: {pid}, Name: {name}, Child Process Count: {len(child_processes)}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Excessive child processes log saved.")

