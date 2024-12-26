"""
Script: log_critical_file_deletion.py
Developer: Ronald Baker
Purpose: Detects and logs attempts to delete critical system files by processes.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import os  # For file path checks
import time  # For periodic polling

# List of critical system files to monitor for deletion attempts
CRITICAL_FILES = ["/etc/passwd", "/etc/hosts", "/etc/sudoers", "C:\\Windows\\System32\\drivers\\etc\\hosts"]

# Output file to save the log of deletion attempts
log_file = "critical_file_deletion_log.txt"

# Function to check if a critical file has been deleted
def is_file_deleted(file_path):
    """
    Checks if a file still exists at the given path.
    """
    return not os.path.exists(file_path)

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Critical File Deletion Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        # Store the initial state of critical files
        file_status = {file_path: not is_file_deleted(file_path) for file_path in CRITICAL_FILES}

        while True:
            for file_path in CRITICAL_FILES:
                # Check if the file has been deleted
                file_exists = not is_file_deleted(file_path)

                if not file_exists and file_status[file_path]:
                    # Log the deletion attempt
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = f"[{timestamp}] Critical File Deleted: {file_path}\n"
                    file.write(log_entry)
                    print(log_entry.strip())  # Print to the console

                    # Update the file's status to reflect it has been deleted
                    file_status[file_path] = False

                elif file_exists and not file_status[file_path]:
                    # File has been restored (optional log for recovery)
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = f"[{timestamp}] Critical File Restored: {file_path}\n"
                    file.write(log_entry)
                    print(log_entry.strip())  # Print to the console

                    # Update the file's status to reflect it is now present
                    file_status[file_path] = True

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Critical file deletion log saved.")

