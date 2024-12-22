"""
Script: monitor_critical_processes.py
Developer: Ronald Baker
Purpose: Monitors critical system processes and logs any failures or terminations.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# List of critical process names to monitor
CRITICAL_PROCESSES = ["sshd", "nginx", "mysql", "explorer.exe", "svchost.exe"]

# Output file to save the log of critical process status
log_file = "critical_processes_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Critical Processes Monitoring Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    # Dictionary to track the last known status of critical processes
    process_status = {proc: False for proc in CRITICAL_PROCESSES}

    try:
        while True:
            # Get the list of running process names
            running_processes = {proc.info["name"] for proc in psutil.process_iter(attrs=["name"])}

            # Check the status of each critical process
            for process in CRITICAL_PROCESSES:
                if process in running_processes:
                    # If the process is running but was previously not running, log recovery
                    if not process_status[process]:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = f"[{timestamp}] Process Recovered: {process}\n"
                        file.write(log_entry)
                        print(log_entry.strip())
                    process_status[process] = True
                else:
                    # If the process is not running but was previously running, log failure
                    if process_status[process]:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = f"[{timestamp}] Process Failed: {process}\n"
                        file.write(log_entry)
                        print(log_entry.strip())
                    process_status[process] = False

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Critical process status log saved.")

