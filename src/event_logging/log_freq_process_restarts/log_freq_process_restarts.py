"""
Script: log_frequent_process_restarts.py
Developer: Ronald Baker
Purpose: Detects and logs processes that restart frequently within a specified time window.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime, timedelta  # For timestamp calculations

# Threshold for frequent restarts (number of restarts within the time window)
RESTART_THRESHOLD = 3
# Time window for monitoring restarts (in seconds)
TIME_WINDOW = 60

# Dictionary to track process restarts (PID -> [start_times])
restart_tracker = {}

def log_frequent_process_restarts(simulated_processes=None):
    """
    Monitors processes for frequent restarts and returns the events as a string.

    Args:
        simulated_processes (list, optional): A list of dictionaries representing
                                              simulated processes for testing.
                                              Each dictionary should have 'pid', 'name', 
                                              and 'create_time' keys.

    Returns:
        str: Log entries for frequent restarts, if any.
    """
    log_entries = []
    process_list = (
        simulated_processes
        if simulated_processes is not None
        else psutil.process_iter(attrs=["pid", "name", "create_time"])
    )

    for process in process_list:
        try:
            # Extract process details
            pid = process["pid"] if simulated_processes else process.info["pid"]
            name = process["name"] if simulated_processes else process.info["name"]
            create_time = (
                process["create_time"]
                if simulated_processes
                else datetime.fromtimestamp(process.info["create_time"])
            )

            # Track process restarts
            if pid not in restart_tracker:
                restart_tracker[pid] = [create_time]
            else:
                restart_tracker[pid].append(create_time)
                restart_tracker[pid] = [
                    t for t in restart_tracker[pid]
                    if (datetime.now() - t).total_seconds() <= TIME_WINDOW
                ]

                if len(restart_tracker[pid]) > RESTART_THRESHOLD:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = (f"[{timestamp}] Frequent Restarts Detected - PID: {pid}, "
                                 f"Name: {name}, Restarts: {len(restart_tracker[pid])}\n")
                    log_entries.append(log_entry)
        except (psutil.NoSuchProcess, psutil.AccessDenied, KeyError):
            continue

    if log_entries:
        return "".join(log_entries)
    return "No frequent restarts detected."

if __name__ == "__main__":
    # Call the function and print the output
    result = log_frequent_process_restarts()
    print(result)
