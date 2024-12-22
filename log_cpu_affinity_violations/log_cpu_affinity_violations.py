"""
Script: log_cpu_affinity_violations.py
Developer: Ronald Baker
Purpose: Tracks CPU affinity of processes and logs violations of assigned CPU cores.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file

# Define a dictionary of processes with their expected CPU affinity
EXPECTED_AFFINITY = {
    "example_process_1": [0, 1],  # Process name and its assigned cores
    "example_process_2": [2, 3]
}

# Output file to save the log of CPU affinity violations
log_file = "cpu_affinity_violations_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"CPU Affinity Violations Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

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
                                     f"Expected: {EXPECTED_AFFINITY[name]}, Current: {current_affinity}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

            except (psutil.NoSuchProcess, psutil.AccessDenied, AttributeError):
                # Skip processes that are inaccessible or don't support affinity
                continue

        print(f"CPU affinity violations log saved to {log_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

