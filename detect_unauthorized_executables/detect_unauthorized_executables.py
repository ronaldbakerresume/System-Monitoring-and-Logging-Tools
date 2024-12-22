"""
Script: detect_unauthorized_executables.py
Developer: Ronald Baker
Purpose: Detects and logs processes using unauthorized executables or scripts.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file

# List of unauthorized executables or script names
UNAUTHORIZED_EXECUTABLES = ["malicious.exe", "unauthorized.py", "hacker_tool", "suspicious_script.sh"]

# Output file to save the log of unauthorized processes
log_file = "unauthorized_executables_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Unauthorized Executables Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        # Iterate through all running processes
        for process in psutil.process_iter(attrs=["pid", "name", "cmdline"]):
            try:
                # Get process details
                pid = process.info["pid"]
                name = process.info["name"]
                cmdline = " ".join(process.info.get("cmdline", []))

                # Check if the process is using an unauthorized executable or script
                if any(unauth in cmdline.lower() for unauth in UNAUTHORIZED_EXECUTABLES):
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = (f"[{timestamp}] Unauthorized Process Detected - PID: {pid}, "
                                 f"Name: {name}, Command: {cmdline}\n")
                    file.write(log_entry)
                    print(log_entry.strip())  # Print to the console

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Skip processes that are inaccessible or have terminated
                continue

        print(f"Unauthorized executables log saved to {log_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

