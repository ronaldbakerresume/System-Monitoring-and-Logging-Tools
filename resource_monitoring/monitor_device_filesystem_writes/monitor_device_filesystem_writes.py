"""
Script: monitor_device_filesystem_writes.py
Developer: Ronald Baker
Purpose: Monitors processes writing to specific devices or filesystems and logs their activities.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process and disk I/O monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Specify devices or filesystems to monitor
MONITORED_FILESYSTEMS = ["/dev/sda1", "C:\\", "/mnt/data"]

# Output file to save the log of processes writing to specified devices/filesystems
log_file = "device_filesystem_write_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Device/Filesystem Write Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name", "io_counters"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]
                    io_counters = process.info.get("io_counters")

                    # If the process has disk write activity
                    if io_counters and io_counters.write_bytes > 0:
                        # Check if the process writes to monitored filesystems/devices
                        for fs in MONITORED_FILESYSTEMS:
                            # Simulate filesystem match (custom logic may be needed for actual mapping)
                            if fs in name or fs in " ".join(process.cmdline()):
                                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                log_entry = (f"[{timestamp}] Process: PID {pid}, Name: {name}, "
                                             f"Write Bytes: {io_counters.write_bytes}\n")
                                file.write(log_entry)
                                print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Device/filesystem write log saved.")

