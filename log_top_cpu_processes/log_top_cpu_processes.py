"""
Script: log_top_cpu_processes.py
Developer: Ronald Baker
Purpose: Continuously logs the top 10 CPU-consuming processes.
Compatible with: Linux, Windows, and Mac OS
"""

import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Output file to save the log of top CPU-consuming processes
log_file = "top_cpu_processes_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Top CPU Processes Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Capture a list of all processes with their CPU usage
            processes = []
            for process in psutil.process_iter(attrs=["pid", "name", "cpu_percent"]):
                try:
                    pid = process.info["pid"]
                    name = process.info["name"]
                    cpu_usage = process.info["cpu_percent"]
                    processes.append((pid, name, cpu_usage))
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    # Skip processes that are inaccessible or have terminated
                    continue

            # Sort processes by CPU usage (descending) and take the top 10
            top_processes = sorted(processes, key=lambda x: x[2], reverse=True)[:10]

            # Log the top processes
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"[{timestamp}] Top 10 CPU-Consuming Processes:\n")
            for pid, name, cpu in top_processes:
                file.write(f"  PID: {pid}, Name: {name}, CPU Usage: {cpu:.2f}%\n")
            file.write("\n")
            print(f"Logged top 10 CPU processes at {timestamp}")

            time.sleep(5)  # Poll every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped. Top CPU process log saved.")

