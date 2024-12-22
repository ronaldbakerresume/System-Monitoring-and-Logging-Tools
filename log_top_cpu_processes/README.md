
# log_top_cpu_processes.py

A Python script that continuously logs the top 10 CPU-consuming processes. This tool is useful for identifying resource-intensive applications and monitoring system performance.

## Features

- **Real-Time Monitoring**: Continuously captures and logs processes with the highest CPU usage.
- **Top Processes**: Focuses on the top 10 CPU-consuming processes for detailed analysis.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.
- **Detailed Logging**: Logs process details (PID, name, and CPU usage) with timestamps.

## How It Works

1. The script uses the `psutil` library to monitor all running processes.
2. It calculates CPU usage for each process and sorts them in descending order.
3. The top 10 CPU-consuming processes are logged to a file and printed to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Run the script:
   ```bash
   python log_top_cpu_processes.py
   ```

3. To stop monitoring, press `Ctrl+C`. The script will save all logged data to the log file.

## Configuration

- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `top_cpu_processes_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

An example log entry might look like:

```
Top CPU Processes Log - 2024-12-22 19:00:00
============================================================
[2024-12-22 19:00:05] Top 10 CPU-Consuming Processes:
  PID: 1234, Name: chrome, CPU Usage: 45.32%
  PID: 5678, Name: python, CPU Usage: 30.45%
  PID: 9101, Name: java, CPU Usage: 15.20%
  PID: 1123, Name: systemd, CPU Usage: 10.25%
  PID: 1314, Name: firefox, CPU Usage: 8.76%
  PID: 1516, Name: docker, CPU Usage: 6.89%
  PID: 1718, Name: explorer.exe, CPU Usage: 4.50%
  PID: 1920, Name: nginx, CPU Usage: 3.89%
  PID: 2122, Name: mysql, CPU Usage: 3.45%
  PID: 2324, Name: redis, CPU Usage: 2.89%
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain process information.
- Processes that terminate quickly or are inaccessible during monitoring are automatically skipped.
- The script runs in a continuous loop for real-time monitoring. To run it periodically, consider scheduling it using a task scheduler (e.g., `cron` on Linux or Task Scheduler on Windows).

## Author

**Ronald Baker**  
A developer focused on building tools for system monitoring and resource optimization.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Optimize your CPU usage efficiently! 🚀
```
