"""
Script: log_process_hierarchy.py
Developer: Ronald Baker
Purpose: Logs parent-child relationships for all active processes.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For system process monitoring
from datetime import datetime  # To timestamp the log file

# Output file to save the log of process hierarchy
log_file = "process_hierarchy_log.txt"

# Open the log file in write mode
with open(log_file, "w") as file:
    file.write(f"Process Hierarchy Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        # Iterate through all running processes
        for process in psutil.process_iter(attrs=["pid", "name", "ppid"]):
            try:
                # Get process details
                pid = process.info["pid"]
                name = process.info["name"]
                ppid = process.info["ppid"]

                # Try to get the parent process details
                try:
                    parent = psutil.Process(ppid)
                    parent_name = parent.name()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    parent_name = "N/A"

                # Log the process hierarchy
                log_entry = (f"Process: PID {pid}, Name: {name} --> "
                             f"Parent: PID {ppid}, Name: {parent_name}\n")
                file.write(log_entry)
                print(log_entry.strip())  # Print to the console

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Skip processes that are inaccessible or have terminated
                continue

        print(f"Process hierarchy logged to {log_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

