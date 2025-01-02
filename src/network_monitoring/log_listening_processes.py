"""
Script: log_listening_processes.py
Developer: Ronald Baker
Purpose: Logs all processes listening on specific network ports and returns as a string.
Compatible with: Linux, Windows, and Mac OS
"""

import os
import subprocess
from datetime import datetime

# List of ports to monitor
MONITORED_PORTS = [22, 80, 443, 8080]  # Add ports of interest

def log_listening_processes():
    """
    Captures processes listening on specific network ports and returns as a string.

    :return: A string containing the log of listening processes.
    """
    log_entries = []
    log_entries.append(f"Listening Process Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_entries.append("=" * 60)

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
                log_entry = f"[{timestamp}] {line.strip()}"
                log_entries.append(log_entry)

    except Exception as e:
        log_entries.append(f"An error occurred: {e}")

    return "\n".join(log_entries)
