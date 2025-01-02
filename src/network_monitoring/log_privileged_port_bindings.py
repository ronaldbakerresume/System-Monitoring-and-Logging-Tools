"""
Script: log_privileged_port_bindings.py
Developer: Ronald Baker
Purpose: Monitors and logs processes attempting to bind to privileged ports (<1024).
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process and connection monitoring
from datetime import datetime  # To timestamp the log file

def log_privileged_port_bindings():
    """
    Monitors and logs processes attempting to bind to privileged ports (<1024) and returns the log as a string.

    :return: A string containing the log of privileged port bindings.
    """
    log_entries = []
    log_entries.append(f"Privileged Port Bindings Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_entries.append("=" * 60)

    try:
        # Iterate through all network connections
        for conn in psutil.net_connections(kind="inet"):
            try:
                # Check if the local address has a privileged port
                if conn.laddr and conn.laddr.port < 1024:
                    pid = conn.pid
                    local_address = f"{conn.laddr.ip}:{conn.laddr.port}"
                    remote_address = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                    status = conn.status

                    # Get the process associated with the connection
                    if pid:
                        process = psutil.Process(pid)
                        name = process.name()

                        # Log the binding attempt
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Privileged Port Binding - PID: {pid}, Name: {name}, "
                                     f"Local Address: {local_address}, Remote Address: {remote_address}, "
                                     f"Status: {status}\n")
                        log_entries.append(log_entry)

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Skip processes that are inaccessible or have terminated
                continue

        return "\n".join(log_entries)

    except Exception as e:
        return f"An error occurred: {e}"

