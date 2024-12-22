
# log_specific_network_access.py

A Python script to monitor and log processes accessing specific IP addresses or domains. This tool is ideal for tracking network activity and identifying connections to critical or sensitive addresses.

## Features

- **Targeted Monitoring**: Monitors processes connecting to specific IP addresses or domains.
- **Real-Time Logging**: Logs process details (PID, name, local and remote addresses) for flagged network connections.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.

## How It Works

1. The script uses the `psutil` library to monitor all active network connections.
2. It checks if any remote address matches a predefined list of monitored IPs or domains.
3. For each match, the associated process details are logged to a file and printed to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Define the list of monitored IP addresses or domains in the script:
   ```python
   MONITORED_IPS = ["192.168.1.1", "10.0.0.1", "example.com"]
   ```

3. Run the script:
   ```bash
   python log_specific_network_access.py
   ```

4. To stop monitoring, press `Ctrl+C`. The script will save all logged data to the log file.

## Configuration

- **Monitored IPs/Domains**: Update the `MONITORED_IPS` list to include the IP addresses or domains you wish to monitor.
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `specific_network_access_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

When a specific network access is detected, a log entry like the following is saved in the log file:

```
Specific Network Access Log - 2024-12-22 20:30:00
============================================================
[2024-12-22 20:30:05] Specific Network Access Detected - PID: 1234, Name: chrome, Local Address: 192.168.1.100:5050, Remote Address: 192.168.1.1:443
[2024-12-22 20:30:10] Specific Network Access Detected - PID: 5678, Name: python, Local Address: 10.0.0.2:6060, Remote Address: 10.0.0.1:80
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain process information or network connections.
- Processes or connections that terminate quickly may not be logged if the polling interval is too long.
- The script runs in a continuous loop for real-time monitoring. To run it periodically, consider scheduling it using a task scheduler (e.g., `cron` on Linux or Task Scheduler on Windows).

## Author

**Ronald Baker**  
A developer dedicated to enhancing system security and network monitoring tools.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Track and secure your network connections effectively! 🌐
```
