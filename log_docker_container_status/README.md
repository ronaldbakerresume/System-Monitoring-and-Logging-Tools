```markdown
# log_docker_container_status.py

A Python script that monitors and logs the statuses of Docker containers. This tool is useful for tracking container activity and ensuring their availability in real time.

## Features

- **Docker Container Monitoring**: Logs the ID, name, and status of all active Docker containers.
- **Real-Time Logging**: Tracks container statuses continuously with timestamps.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS (requires Docker).

## How It Works

1. The script uses the `docker ps` command to fetch the statuses of running Docker containers.
2. Parses the output to extract container IDs, names, and statuses.
3. Logs these details to a file and optionally prints them to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Docker**:
  - Docker must be installed and running.
  - Ensure the user has sufficient permissions to run Docker commands (e.g., part of the `docker` group on Linux).

## Usage

1. Ensure Docker is installed and running:
   ```bash
   docker --version
   ```

2. Run the script:
   ```bash
   python log_docker_container_status.py
   ```

3. Check the log file for container statuses:
   ```bash
   cat docker_container_status_log.txt
   ```

## Configuration

- **Polling Interval**: The script polls every 5 seconds by default. Update the `time.sleep(5)` line to adjust the interval.
- **Log File**: Logs are saved to `docker_container_status_log.txt` by default. Update the `log_file` variable in the script to use a different file name or path.

## Example Log File

When Docker containers are detected, entries like the following are saved in the log file:

```
Docker Container Status Log - 2024-12-23 02:15:00
============================================================
[2024-12-23 02:15:05] Docker Container - ID: abc123, Name: web_app, Status: Up 5 minutes
[2024-12-23 02:15:05] Docker Container - ID: def456, Name: database, Status: Exited (0) 2 minutes ago
```

## Notes

- **Permission Requirements**:
  - On Linux, non-root users may need to be added to the `docker` group to execute Docker commands without `sudo`:
    ```bash
    sudo usermod -aG docker $USER
    ```
    Then log out and log back in for the changes to take effect.
- The script logs only running containers. Containers that are stopped or paused are included only if their statuses are retrievable via `docker ps`.

## Limitations

- The script depends on the availability of the Docker CLI. If Docker is not installed or accessible, the script will not run.
- Stopped containers may not appear unless explicitly included with additional Docker commands (e.g., `docker ps -a`).

## Author

**Ronald Baker**  
A developer focused on creating tools for container monitoring and system reliability.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Track Docker container statuses effectively! 🚢
```