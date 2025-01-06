"""
Script: log_hardware_interactions.py
Developer: Ronald Baker
Purpose: Monitors and logs processes interacting with hardware devices like USB and network interfaces.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process and connection monitoring
from datetime import datetime  # To timestamp the log file

# Output file to save the log of hardware interactions
log_file = "hardware_interactions_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Hardware Interactions Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        # Iterate through all network connections
        for conn in psutil.net_connections(kind="inet"):
            try:
                # Get connection details
                pid = conn.pid
                local_address = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                remote_address = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                status = conn.status

                # Get the process associated with the connection
                if pid:
                    process = psutil.Process(pid)
                    name = process.name()

                    # Log the connection and process details
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = (f"[{timestamp}] Process: PID {pid}, Name: {name}, "
                                 f"Local Address: {local_address}, Remote Address: {remote_address}, "
                                 f"Status: {status}\n")
                    file.write(log_entry)
                    print(log_entry.strip())  # Print to the console

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Skip processes that are inaccessible or have terminated
                continue

        print(f"Hardware interaction log saved to {log_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

