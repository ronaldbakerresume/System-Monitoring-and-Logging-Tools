"""
Script: log_process_count_changes.py
Developer: Ronald Baker
Purpose: Continuously monitors and logs changes in the total number of running processes.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For system process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Output file to save the log of process count changes
log_file = "process_count_changes_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Process Count Changes Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        # Initialize the previous process count
        previous_count = len(psutil.pids())

        while True:
            # Get the current process count
            current_count = len(psutil.pids())

            # Check for changes in the process count
            if current_count != previous_count:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                change = current_count - previous_count
                direction = "increased" if change > 0 else "decreased"
                log_entry = (f"[{timestamp}] Process count {direction} by {abs(change)}: "
                             f"New count = {current_count}\n")

                # Log the change to the file
                file.write(log_entry)
                print(log_entry.strip())  # Print to the console

                # Update the previous count
                previous_count = current_count

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Process count change log saved.")

