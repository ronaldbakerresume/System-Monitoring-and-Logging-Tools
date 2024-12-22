
# monitor_critical_processes.py

A Python script designed to monitor critical system processes and log any failures or terminations. It also logs when processes recover after a failure. This tool is ideal for ensuring the availability of essential services and processes.

## Features

- **Real-Time Monitoring**: Tracks critical processes and detects when they fail or recover.
- **Customizable Watchlist**: Specify the list of critical processes to monitor.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.
- **Detailed Logging**: Logs process failures and recoveries with timestamps.

## How It Works

1. The script continuously polls the list of running processes using the `psutil` library.
2. It checks whether each critical process is running or has terminated.
3. Any status change (failure or recovery) is logged to a file and printed to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Define the list of critical processes in the script:
   ```python
   CRITICAL_PROCESSES = ["sshd", "nginx", "mysql", "explorer.exe", "svchost.exe"]
   ```

3. Run the script:
   ```bash
   python monitor_critical_processes.py
   ```

4. To stop monitoring, press `Ctrl+C`. The script will save all logged data to the log file.

## Configuration

- **Critical Processes**: Update the `CRITICAL_PROCESSES` list in the script to include the names of the processes you wish to monitor.
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `critical_processes_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

When a critical process fails or recovers, a log entry like the following is saved in the log file:

```
Critical Processes Monitoring Log - 2024-12-22 17:00:00
============================================================
[2024-12-22 17:00:05] Process Failed: sshd
[2024-12-22 17:00:10] Process Recovered: sshd
[2024-12-22 17:00:15] Process Failed: mysql
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain process information.
- Processes that terminate quickly or restart rapidly may result in consecutive failure and recovery logs.
- The script runs in a continuous loop for real-time monitoring. To run it periodically, consider scheduling it using a task scheduler (e.g., `cron` on Linux or Task Scheduler on Windows).

## Author

**Ronald Baker**  
A developer focused on creating tools for system reliability and performance monitoring.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Stay on top of your critical processes! ⚙️
```
