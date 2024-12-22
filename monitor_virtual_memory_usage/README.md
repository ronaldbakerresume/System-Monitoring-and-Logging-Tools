
# monitor_virtual_memory_usage.py

A Python script designed to monitor processes consuming significant virtual memory and log their details to a file. This tool is ideal for system administrators and developers who need to track memory-intensive processes in real-time.

## Features

- **Real-Time Monitoring**: Continuously monitors processes for high virtual memory usage.
- **Customizable Threshold**: Easily adjust the virtual memory usage threshold in megabytes.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.
- **Logging**: Saves details of high-memory processes to a timestamped log file.
- **Console Output**: Provides live updates of monitored processes in the terminal.

## How It Works

1. The script uses the `psutil` library to access system and process information.
2. It iterates over all running processes, checking their virtual memory usage.
3. If a process exceeds the defined memory threshold, its details (PID, name, and memory usage) are logged to a file and printed to the console.

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
   python monitor_virtual_memory_usage.py
   ```

3. To stop monitoring, press `Ctrl+C`. The script will save all logged data to a file.

## Configuration

- **Threshold**: Modify the `VIRTUAL_MEMORY_THRESHOLD_MB` variable in the script to set the threshold for significant virtual memory usage (default: 500 MB).
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `high_virtual_memory_processes_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

When a process exceeds the memory threshold, a log entry like the following is saved in the log file:

```
High Virtual Memory Usage Log - 2024-12-22 10:30:00
============================================================
[2024-12-22 10:30:05] Process: PID 1234, Name: python, Virtual Memory: 512.34 MB
[2024-12-22 10:30:10] Process: PID 5678, Name: chrome, Virtual Memory: 1024.56 MB
```

## Notes

- Processes that terminate or are inaccessible during monitoring (due to permissions) are automatically skipped.
- The script provides live updates in the console for real-time monitoring.

## Author

**Ronald Baker**  
A developer focused on creating tools for efficient system monitoring and performance optimization.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Happy monitoring! 📈
```
