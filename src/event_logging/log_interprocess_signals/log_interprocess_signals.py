"""
Script: log_interprocess_signals.py
Developer: Ronald Baker
Purpose: Tracks and logs inter-process communication signals such as SIGINT and SIGTERM.
Compatible with: Linux, Windows, and Mac OS
"""

import os
import signal  # For signal handling
import time  # To keep the script running
from datetime import datetime  # To timestamp the log file

# Output file to save the log of inter-process communication signals
log_file = "interprocess_signals_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    # Write the header
    file.write(f"Inter-Process Signal Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

# Signal handler function
def signal_handler(signum, frame):
    """
    Handles received signals and logs their details to a file.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    signal_name = signal.Signals(signum).name  # Convert signal number to name
    log_entry = f"[{timestamp}] Received Signal: {signal_name} (Number: {signum})\n"

    # Log the signal details
    with open(log_file, "a") as file:
        file.write(log_entry)
    print(log_entry.strip())  # Also print to the console

# Map signals to the handler
signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C (Interrupt Signal)
signal.signal(signal.SIGTERM, signal_handler)  # Handle termination signals
if hasattr(signal, "SIGHUP"):  # Handle hang-up signals (Linux/Mac only)
    signal.signal(signal.SIGHUP, signal_handler)

# Infinite loop to keep the script running and monitoring signals
print("Signal logger is running. Press Ctrl+C to test SIGINT.")
try:
    while True:
        time.sleep(1)  # Keep the script running without excessive CPU usage
except KeyboardInterrupt:
    print("Signal monitoring stopped.")

