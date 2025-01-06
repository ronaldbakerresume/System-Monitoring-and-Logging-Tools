"""
Script: log_cpu_affinity_violations.py
Developer: Ronald Baker
Purpose: Tracks CPU affinity of processes and returns violations of assigned CPU cores as a formatted string.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log entries

# Define a dictionary of processes with their expected CPU affinity
EXPECTED_AFFINITY = {
    "example_process_1": [0, 1],  # Process name and its assigned cores
    "example_process_2": [2, 3]
}

def log_cpu_affinity_violations():
    """
    Checks the CPU affinity of processes and returns a log of violations as a formatted string.

    Returns:
        str: Formatted string containing details of CPU affinity violations.
    """
    log_entries = []
    timestamp_header = f"CPU Affinity Violations Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    log_entries.append(timestamp_header)
    log_entries.append("=" * 60)

    try:
        # Iterate through all running processes
        for process in psutil.process_iter(attrs=["pid", "name"]):
            try:
                # Get process details
                pid = process.info["pid"]
                name = process.info["name"]

                # Check if the process is in the expected affinity dictionary
                if name in EXPECTED_AFFINITY:
                    # Get the current CPU affinity of the process
                    current_affinity = process.cpu_affinity()  # List of CPU cores

                    # Check if the current affinity matches the expected affinity
                    if set(current_affinity) != set(EXPECTED_AFFINITY[name]):
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] CPU Affinity Violation - PID: {pid}, Name: {name}, "
                                     f"Expected: {EXPECTED_AFFINITY[name]}, Current: {current_affinity}")
                        log_entries.append(log_entry)

            except (psutil.NoSuchProcess, psutil.AccessDenied, AttributeError):
                # Skip processes that are inaccessible or don't support affinity
                continue

    except Exception as e:
        log_entries.append(f"An error occurred: {e}")

    return "\n".join(log_entries)

