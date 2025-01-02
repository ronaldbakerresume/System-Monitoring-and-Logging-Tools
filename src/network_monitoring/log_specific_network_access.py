"""
Script: log_specific_network_access.py
Developer: Ronald Baker
Purpose: Monitors and logs processes accessing specific IP addresses or domains.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process and connection monitoring
from datetime import datetime  # To timestamp the log file

# List of specific IP addresses or domains to monitor
MONITORED_IPS = ["192.168.1.1", "10.0.0.1", "example.com"]

# Output file to save the log of specific network access
log_file = "specific_network_access_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Specific Network Access Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Iterate through all network connections
            for conn in psutil.net_connections(kind="inet"):
                try:
                    # Get connection details
                    pid = conn.pid
                    local_address = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                    remote_address = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"

                    # Check if the remote IP matches any monitored IP or domain
                    if conn.raddr and any(ip in conn.raddr.ip for ip in MONITORED_IPS):
                        # Get the associated process details
                        if pid:
                            process = psutil.Process(pid)
                            name = process.name()
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            log_entry = (f"[{timestamp}] Specific Network Access Detected - "
                                         f"PID: {pid}, Name: {name}, Local Address: {local_address}, "
                                         f"Remote Address: {remote_address}\n")
                            file.write(log_entry)
                            print(log_entry.strip())  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Specific network access log saved.")

