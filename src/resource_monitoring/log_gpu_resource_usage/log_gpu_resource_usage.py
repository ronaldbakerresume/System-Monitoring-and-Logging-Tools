"""
Script: log_gpu_resource_usage.py
Developer: Ronald Baker
Purpose: Tracks and logs processes consuming GPU resources.
Compatible with: Linux, Windows, and Mac OS (requires NVIDIA GPUs and drivers).
"""

import os
import subprocess  # For running system commands
from datetime import datetime  # To timestamp the log file

# Output file to save the log of GPU resource usage
log_file = "gpu_resource_usage_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"GPU Resource Usage Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Run the NVIDIA SMI command to get GPU usage
            try:
                result = subprocess.run(
                    ["nvidia-smi", "--query-compute-apps=pid,process_name,used_memory", "--format=csv,noheader,nounits"],
                    stdout=subprocess.PIPE,
                    text=True,
                )
                output = result.stdout.strip()

                # Parse the output and log the processes using GPU resources
                if output:
                    for line in output.splitlines():
                        pid, process_name, used_memory = line.split(", ")
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] GPU Process - PID: {pid}, Name: {process_name}, "
                                     f"Memory Usage: {used_memory} MiB\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

            except FileNotFoundError:
                print("Error: NVIDIA SMI command not found. Ensure NVIDIA drivers are installed.")
                break

            except Exception as e:
                print(f"An error occurred while fetching GPU usage: {e}")
                break

            # Poll every 5 seconds
            time.sleep(5)

    except KeyboardInterrupt:
        print("Monitoring stopped. GPU resource usage log saved.")

