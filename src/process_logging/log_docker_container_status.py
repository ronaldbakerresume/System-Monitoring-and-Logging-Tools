"""
Script: log_docker_container_status.py
Developer: Ronald Baker
Purpose: Monitors Docker containerized processes and logs their statuses.
Compatible with: Linux, Windows, and Mac OS (requires Docker).
"""

import subprocess  # For running Docker commands
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Output file to save the log of Docker container statuses
log_file = "docker_container_status_log.txt"

# Open the log file in append mode
with open(log_file, "a") as file:
    file.write(f"Docker Container Status Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("=" * 60 + "\n")

    try:
        while True:
            # Run the Docker PS command to get container statuses
            try:
                result = subprocess.run(
                    ["docker", "ps", "--format", "{{.ID}},{{.Names}},{{.Status}}"],
                    stdout=subprocess.PIPE,
                    text=True,
                )
                output = result.stdout.strip()

                # Parse the output and log the container statuses
                if output:
                    for line in output.splitlines():
                        container_id, container_name, status = line.split(",")
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Docker Container - ID: {container_id}, "
                                     f"Name: {container_name}, Status: {status}\n")
                        file.write(log_entry)
                        print(log_entry.strip())  # Print to the console

            except FileNotFoundError:
                print("Error: Docker command not found. Ensure Docker is installed and running.")
                break

            except Exception as e:
                print(f"An error occurred while fetching Docker statuses: {e}")
                break

            # Poll every 5 seconds
            time.sleep(5)

    except KeyboardInterrupt:
        print("Monitoring stopped. Docker container status log saved.")

