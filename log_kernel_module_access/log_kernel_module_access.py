"""
Script: log_kernel_module_access.py
Developer: Ronald Baker
Purpose: Monitors and logs processes accessing specific kernel modules or drivers.
Compatible with: Linux, Windows, and Mac OS (Linux-specific kernel module monitoring).
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# List of kernel modules or drivers to monitor (Linux-specific example)
MONITORED_MODULES = ["/proc/modules", "/lib/modules", "/sys/module"]

# Output file to save the log of kernel module access
log_file = "kernel_module_access_log.txt"

# Function to check if a process accesses monitored kernel modules
def is_accessing_kernel_module(proc):
    """
    Checks if a process has opened files in monitored kernel module paths.
    """
    try:
        # Iterate through all open files of the process
        for file in proc.open_files():
            # Check if the file path starts with any monitored module
            for module in MONITORED_MODULES:
                if file.path.startswith(module):
                    return True, file.path
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Skip processes that are inaccessible or have terminated
        pass
    return False, None

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Kernel Module Access Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name"]):
                try:
                    # Check if the process accesses monitored kernel modules
                    accessing, path = is_accessing_kernel_module(process)
                    if accessing:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Process: PID {process.info['pid']}, "
                                     f"Name: {process.info['name']}, Accessed Path: {path}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Kernel module access log saved.")

