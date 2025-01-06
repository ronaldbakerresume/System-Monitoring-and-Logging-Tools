"""
Script: log_unauthorized_execution.py
Developer: Ronald Baker
Purpose: Monitors and logs processes executing from unauthorized directories.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file

# List of authorized directories for execution
AUTHORIZED_DIRECTORIES = ["/usr/bin", "/bin", "C:\\Windows\\System32", "/usr/sbin"]

# Output file to save the log of unauthorized executions
log_file = "unauthorized_execution_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Unauthorized Execution Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name", "exe"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]
                    exe_path = process.info.get("exe", "N/A")

                    # Check if the executable path is outside authorized directories
                    if exe_path != "N/A" and not any(exe_path.startswith(auth_dir) for auth_dir in AUTHORIZED_DIRECTORIES):
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Unauthorized Execution Detected - "
                                     f"PID: {pid}, Name: {name}, Executable Path: {exe_path}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Unauthorized execution log saved.")

