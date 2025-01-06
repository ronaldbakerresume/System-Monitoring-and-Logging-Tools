"""
Script: log_docker_container_status.py
Developer: Ronald Baker
Purpose: Monitors Docker containerized processes and returns their statuses as a formatted string.
Compatible with: Linux, Windows, and Mac OS (requires Docker).
"""

import subprocess  # For running Docker commands
from datetime import datetime  # To timestamp the log entries

def log_docker_container_status():
    """
    Fetches the status of all running Docker containers and returns a formatted string log.

    Returns:
        str: Formatted string containing details of Docker container statuses.
    """
    log_entries = []
    timestamp_header = f"Docker Container Status Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    log_entries.append(timestamp_header)
    log_entries.append("=" * 60)

    try:
        # Run the Docker PS command to get container statuses
        result = subprocess.run(
            ["docker", "ps", "--format", "{{.ID}},{{.Names}},{{.Status}}"],
            stdout=subprocess.PIPE,
            text=True,
            check=True
        )
        output = result.stdout.strip()

        # Parse the output and log the container statuses
        if output:
            for line in output.splitlines():
                container_id, container_name, status = line.split(",")
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_entry = (f"[{timestamp}] Docker Container - ID: {container_id}, "
                             f"Name: {container_name}, Status: {status}")
                log_entries.append(log_entry)

        else:
            log_entries.append(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] No running Docker containers detected.")

    except FileNotFoundError:
        log_entries.append("Error: Docker command not found. Ensure Docker is installed and running.")

    except subprocess.CalledProcessError as e:
        log_entries.append(f"An error occurred while fetching Docker statuses: {e}")

    return "\n".join(log_entries)
