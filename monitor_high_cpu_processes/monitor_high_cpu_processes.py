"""
Script: monitor_high_cpu_processes.py
Developer: Ronald Baker
Purpose: Monitors processes with high CPU usage and logs their details to a file.
Compatible with: Linux, Windows, and Mac OS
"""

import os  # For OS-specific operations
import subprocess  # To execute system commands
from datetime import datetime  # To timestamp the log file

# Threshold for high CPU usage (percentage)
CPU_THRESHOLD = 10.0

# Output file to save the log of high CPU usage processes
log_file = "high_cpu_processes_log.txt"

# Open the log file in write mode
with open(log_file, "w") as file:
    # Add a header with a timestamp
    file.write(f"High CPU Process Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    # Determine the command to monitor processes based on the operating system
    if os.name == "nt":  # For Windows
        command = ["wmic", "process", "get", "ProcessId,Name,PercentProcessorTime,CommandLine"]
    else:  # For Linux and MacOS
        command = ["ps", "-eo", "pid,comm,%cpu,args"]

    # Execute the command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

    # Parse and filter the command output
    for line in result.stdout.splitlines():
        # Skip the header or empty lines
        if "PID" in line or not line.strip():
            continue

        try:
            # For Linux/MacOS: Split the output into columns
            if os.name != "nt":
                columns = line.split(maxsplit=3)
                pid, name, cpu, args = columns[0], columns[1], float(columns[2]), columns[3]
            else:  # For Windows: Adjust parsing logic for wmic output
                columns = line.split(maxsplit=3)
                pid, name, cpu, args = columns[0], columns[1], float(columns[2]), columns[3]

            # Log processes exceeding the CPU threshold
            if float(cpu) > CPU_THRESHOLD:
                file.write(f"PID: {pid}, Name: {name}, CPU: {cpu}%, Command: {args}\n")
        except (ValueError, IndexError):
            # Skip lines that don't conform to the expected format
            continue

print(f"High CPU processes logged to {log_file}")

