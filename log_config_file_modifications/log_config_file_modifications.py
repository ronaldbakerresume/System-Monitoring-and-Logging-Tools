"""
Script: log_config_file_modifications.py
Developer: Ronald Baker
Purpose: Detects and logs processes attempting to modify critical system configuration files.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# List of critical system configuration files to monitor
CONFIG_FILES = ["/etc/passwd", "/etc/hosts", "/etc/sudoers", "C:\\Windows\\System32\\drivers\\etc\\hosts"]

# Output file to save the log of configuration file modification attempts
log_file = "config_file_modifications_log.txt"

# Function to check if a process is accessing monitored configuration files
def is_modifying_config_file(proc):
    """
    Checks if a process has opened monitored configuration files for writing.
    """
    try:
        # Iterate through all open files of the process
        for file in proc.open_files():
            # Check if the file path matches any critical configuration file
            for config_file in CONFIG_FILES:
                if file.path == config_file and "w" in file.mode:  # Check for write mode
                    return True, file.path
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Skip processes that are inaccessible or have terminated
        pass
    return False, None

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Configuration File Modification Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name"]):
                try:
                    # Check if the process is modifying any monitored configuration file
                    modifying, path = is_modifying_config_file(process)
                    if modifying:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Configuration File Modification Detected - "
                                     f"PID: {process.info['pid']}, Name: {process.info['name']}, "
                                     f"File: {path}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Configuration file modification log saved.")

