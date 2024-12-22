```markdown
# log_open_file_descriptors.py

A Python script that detects and logs file descriptors opened by processes. This tool helps in monitoring resource usage and troubleshooting file-related issues in running applications.

## Features

- **Open File Descriptor Tracking**: Monitors and logs the open files for each running process.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS (with platform-specific limitations).
- **Detailed Logging**: Logs process details (PID, name) and each open file's path and mode.

## How It Works

1. The script uses the `psutil` library to access details about all running processes.
2. For each process, it retrieves the list of open file descriptors (if accessible).
3. Logs the process details and its open files to a text file, along with a timestamp.

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
   python log_open_file_descriptors.py
   ```

3. Check the log file for open file descriptors:
   ```bash
   cat open_file_descriptors_log.txt
   ```

## Configuration

- **Log File**: Logs are saved to `open_file_descriptors_log.txt` by default. Update the `log_file` variable in the script to use a different file name or path.

## Example Log File

When open file descriptors are detected, a log entry like the following is saved in the log file:

```
Open File Descriptors Log - 2024-12-22 23:00:00
============================================================
[2024-12-22 23:00:05] Process: PID 1234, Name: python
  Open File: /home/user/logs/app.log, Mode: r
  Open File: /home/user/config/app.cfg, Mode: w

[2024-12-22 23:00:10] Process: PID 5678, Name: nginx
  Open File: /var/log/nginx/access.log, Mode: r
  Open File: /var/log/nginx/error.log, Mode: r
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain process information or open files.
- Processes that terminate quickly or do not open files may not appear in the log.

## Limitations

- Some processes, especially on restricted systems, may not expose their open file descriptors due to permission restrictions or platform-specific limitations.
- The script captures a snapshot of open files at a point in time. Rapidly opening and closing files may not be captured if the polling interval is too long.

## Author

**Ronald Baker**  
A developer committed to creating tools for resource monitoring and debugging.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Monitor and analyze open file descriptors effectively! 📂
```