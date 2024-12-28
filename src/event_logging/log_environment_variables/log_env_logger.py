"""
Script: environment_logger.py
Developer: Ronald Baker
Purpose: Captures and returns the environment variables of specific processes as a string.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log entries

# List of specific process names to monitor
MONITORED_PROCESSES = ["nginx", "mysql", "python", "explorer.exe"]

def log_environment_variables():
    """
    Captures and returns the environment variables of monitored processes as a string.

    :return: A string containing the log of environment variables.
    """
    log_entries = []
    log_entries.append(f"Process Environment Variables Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_entries.append("=" * 60)

    try:
        # Iterate through all running processes
        for process in psutil.process_iter(attrs=["pid", "name"]):
            try:
                # Get process details
                pid = process.info["pid"]
                name = process.info["name"]

                # Check if the process is in the monitored list
                if name in MONITORED_PROCESSES:
                    # Get the environment variables of the process
                    env_vars = process.environ()

                    # Create a log entry
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = f"[{timestamp}] Process: PID {pid}, Name: {name}"
                    log_entries.append(log_entry)

                    for key, value in env_vars.items():
                        log_entries.append(f"  {key}={value}")

                    log_entries.append("")  # Blank line for separation

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Skip processes that are inaccessible or have terminated
                continue

    except Exception as e:
        log_entries.append(f"An error occurred: {e}")

    return "\n".join(log_entries)

