"""
Script: monitor_disk_io_processes.py
Developer: Ronald Baker
Purpose: Tracks processes consuming excessive disk I/O and logs their statistics.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process and disk I/O monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Threshold for high disk I/O usage (in bytes per second)
DISK_IO_THRESHOLD = 1024 * 1024  # 1 MB per second

# Output file to save the log of high disk I/O processes
log_file = "high_disk_io_processes_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"High Disk I/O Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name"]):
                try:
                    # Get the process's disk I/O statistics
                    io_counters = process.io_counters()
                    read_bytes = io_counters.read_bytes  # Bytes read by the process
                    write_bytes = io_counters.write_bytes  # Bytes written by the process

                    # Check if the process exceeds the disk I/O threshold
                    if read_bytes + write_bytes > DISK_IO_THRESHOLD:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] PID: {process.pid}, Name: {process.info['name']}, "
                                     f"Read: {read_bytes} bytes, Write: {write_bytes} bytes\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. High disk I/O log saved.")

