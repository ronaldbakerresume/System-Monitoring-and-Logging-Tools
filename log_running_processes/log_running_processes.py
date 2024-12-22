"""
Script: log_running_processes.py
Developer: Ronald Baker
Purpose: Logs all currently running processes and their metadata (PID, name, command) to a text file.
Compatible with: Linux, Windows, and Mac OS
"""

import os  # For cross-platform compatibility
import subprocess  # To execute system commands
from datetime import datetime  # To timestamp the log file

# Output file to save the process metadata
log_file = "running_processes_log.txt"

# Open the log file in write mode
with open(log_file, "w") as file:
    # Add a header with a timestamp
    file.write(f"Process Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 50 + "\n")

    # Determine the command to list processes based on the operating system
    if os.name == "nt":  # For Windows
        command = ["tasklist"]
    else:  # For Linux and MacOS
        command = ["ps", "-eo", "pid,comm,args"]

    # Execute the command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

    # Write the command output to the log file
    file.write(result.stdout)

print(f"Process metadata logged to {log_file}")

