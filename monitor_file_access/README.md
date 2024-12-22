
# monitor_file_access.py

A Python script designed to monitor processes accessing specific files or directories and log their activities. This tool is particularly useful for detecting unauthorized or unexpected access to sensitive resources.

## Features

- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.
- **Real-Time Monitoring**: Captures processes accessing a specified file or directory.
- **Detailed Logging**: Logs process details (e.g., name, path, and activity) to a timestamped file.
- **Customizable Target**: Monitor any file or directory by specifying its path.

## How It Works

1. The script runs platform-specific commands to detect processes accessing the specified file or directory.
   - **Linux/macOS**: Uses the `lsof` command.
   - **Windows**: Uses PowerShell's `Get-Process` command.
2. The details of accessing processes are logged to a file with timestamps.
3. The script continuously monitors in real-time until manually terminated.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `lsof` command-line tool (Linux/macOS, pre-installed on most systems)
  - PowerShell (Windows, included in modern Windows versions)

## Usage

1. Define the file or directory to monitor:
   ```python
   monitor_target = "/path/to/monitor"  # For Linux/macOS
   monitor_target = "C:\\Path\\To\\Monitor"  # For Windows
   ```

2. Run the script:
   ```bash
   python monitor_file_access.py
   ```

3. To stop monitoring, press `Ctrl+C`. The script will save all logged data to the log file.

## Configuration

- **Monitoring Target**: Update the `monitor_target` variable to specify the file or directory to monitor.
- **Log File**: Logs are saved to `file_access_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

An example log entry might look like:

```
File Access Log - 2024-12-22 14:00:00
============================================================
[2024-12-22 14:00:05] COMMAND     PID    USER   FD   TYPE DEVICE SIZE/OFF    NODE NAME
[2024-12-22 14:00:05] python3     1234   user   cwd   DIR  8,2    4096     100663296 /path/to/monitor
```

## Notes

- **Permission Requirements**:
  - The script may require elevated permissions (e.g., `sudo` on Linux/macOS) to access all processes.
  - On Windows, run the script as an administrator to ensure proper PowerShell execution.
- **Platform-Specific Commands**:
  - Linux/macOS: Relies on `lsof`, which provides detailed information about open files.
  - Windows: Uses a PowerShell script to query processes interacting with the target path.
- The script runs in a continuous loop for real-time monitoring. To run it periodically, consider scheduling it using a task scheduler (e.g., `cron` on Linux or Task Scheduler on Windows).

## Author

**Ronald Baker**  
A developer dedicated to building tools for system monitoring and enhancing resource security.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Stay vigilant! 🔒
```
