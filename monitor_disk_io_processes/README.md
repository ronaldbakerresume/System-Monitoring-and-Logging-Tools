
# monitor_disk_io_processes.py

A Python script designed to monitor processes with high disk I/O activity and log their statistics. This tool is useful for identifying resource-intensive processes affecting disk performance.

## Features

- **Real-Time Monitoring**: Tracks processes consuming excessive disk I/O.
- **Customizable Thresholds**: Set thresholds for read and write I/O to suit specific needs.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.
- **Detailed Logging**: Logs process details (PID, name, read and write bytes) to a timestamped file.

## How It Works

1. The script uses the `psutil` library to retrieve disk I/O statistics for running processes.
2. It checks if the total disk I/O (read + write bytes) exceeds a predefined threshold.
3. If a process surpasses the threshold, its details are logged to a file and printed to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Configure the disk I/O threshold in the script:
   ```python
   DISK_IO_THRESHOLD = 1024 * 1024  # Threshold in bytes per second (1 MB/s)
   ```

3. Run the script:
   ```bash
   python monitor_disk_io_processes.py
   ```

4. To stop monitoring, press `Ctrl+C`. The script will save all logged data to the log file.

## Configuration

- **Threshold**: Modify the `DISK_IO_THRESHOLD` variable in the script to set the limit for high disk I/O.
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `high_disk_io_processes_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

When a process exceeds the disk I/O threshold, a log entry like the following is saved in the log file:

```
High Disk I/O Log - 2024-12-22 15:00:00
============================================================
[2024-12-22 15:00:05] PID: 1234, Name: chrome, Read: 1200000 bytes, Write: 800000 bytes
[2024-12-22 15:00:10] PID: 5678, Name: python, Read: 2000000 bytes, Write: 1500000 bytes
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain process statistics.
- Processes that terminate or are inaccessible during monitoring are automatically skipped.
- The script runs in a continuous loop for real-time monitoring. To run it periodically, consider scheduling it with a task scheduler (e.g., `cron` on Linux or Task Scheduler on Windows).

## Author

**Ronald Baker**  
A developer committed to creating tools for monitoring and optimizing system performance.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Keep your disk operations optimized! 📂
```
