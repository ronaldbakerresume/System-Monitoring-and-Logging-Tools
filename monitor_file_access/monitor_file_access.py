"""
Script: monitor_file_access.py
Developer: Ronald Baker
Purpose: Monitors processes accessing specific files or directories and logs their activities.
Compatible with: Linux, Windows, and Mac OS
"""

import os  # For OS-specific operations
import subprocess  # To execute system commands
from datetime import datetime  # To timestamp the log file

# Directory or file to monitor
monitor_target = "/path/to/monitor" if os.name != "nt" else "C:\\Path\\To\\Monitor"

# Output file to save the log of file access activities
log_file = "file_access_log.txt"

# Function to monitor file access
def monitor_file_access(target):
    """
    Monitors processes accessing the specified target file or directory.
    """
    if os.name == "nt":  # For Windows
        command = f"powershell -Command \"Get-Process | Where-Object {{$_.Path -like '*{target}*'}}\""
    else:  # For Linux and MacOS
        command = f"lsof +D {target}"

    # Execute the command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

    # Return the output as a list of lines
    return result.stdout.splitlines()

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"File Access Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Capture the processes accessing the target
            accessed_processes = monitor_file_access(monitor_target)

            # Log each process accessing the target
            for line in accessed_processes:
                if line.strip():  # Skip empty lines
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    file.write(f"[{timestamp}] {line.strip()}\n")
                    print(f"Access detected: {line.strip()}")

    except KeyboardInterrupt:
        # Handle script termination gracefully
        print("Monitoring stopped. File access log saved.")

