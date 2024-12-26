"""
Script: log_environment_variables.py
Developer: Ronald Baker
Purpose: Captures and logs the environment variables of specific processes.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file

# List of specific process names to monitor
MONITORED_PROCESSES = ["nginx", "mysql", "python", "explorer.exe"]

# Output file to save the log of environment variables
log_file = "process_environment_variables_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Process Environment Variables Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        # Iterate through all running processes
        for process in psutil.process_iter(attrs=["pid", "name"]):
            try:
                # Get process details
                pid = process.info["pid"]
                name = process.info["name"]

                # Check if the process is in the monitored list
                if name in MONITORED_PROCESSES:
                    # Get the environment variables of the process
                    env_vars = process.environ()

                    # Log the environment variables
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = f"[{timestamp}] Process: PID {pid}, Name: {name}\n"
                    file.write(log_entry)
                    for key, value in env_vars.items():
                        file.write(f"  {key}={value}\n")
                    file.write("\n")
                    print(f"Logged environment variables for PID {pid}, Name: {name}")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Skip processes that are inaccessible or have terminated
                continue

        print(f"Environment variables log saved to {log_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

