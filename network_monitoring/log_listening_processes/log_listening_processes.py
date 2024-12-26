"""
Script: log_listening_processes.py
Developer: Ronald Baker
Purpose: Logs all processes listening on specific network ports.
Compatible with: Linux, Windows, and Mac OS
"""

import os
import subprocess  # To execute system commands
from datetime import datetime  # To timestamp the log file

# List of ports to monitor
MONITORED_PORTS = [22, 80, 443, 8080]  # Add ports of interest

# Output file to save the log of listening processes
log_file = "listening_processes_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Listening Process Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    # Determine the command to list listening processes based on the operating system
    if os.name == "nt":  # For Windows
        command = ["netstat", "-ano"]  # Show all connections with process IDs
    else:  # For Linux and MacOS
        command = ["netstat", "-tuln"]  # Show all listening ports

    try:
        # Execute the command and capture the output
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

        # Parse the command output
        for line in result.stdout.splitlines():
            if any(f":{port}" in line for port in MONITORED_PORTS):  # Check if any monitored port is in the line
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_entry = f"[{timestamp}] {line.strip()}\n"
                file.write(log_entry)  # Write to log file
                print(log_entry.strip())  # Print to the console

    except Exception as e:
        print(f"An error occurred: {e}")

print(f"Listening process log saved to {log_file}")

