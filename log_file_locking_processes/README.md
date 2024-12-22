# log_file_locking_processes.py

A Python script that monitors and logs processes holding locks on specific files. This tool helps in identifying processes that are using critical or sensitive files, which may be useful for debugging or security auditing.

## Features

- **File Lock Detection**: Tracks processes holding locks on a predefined list of critical files.
- **Real-Time Logging**: Logs process details (PID, name, and file path) with timestamps.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.

## How It Works

1. The script uses the `psutil` library to monitor processes and their open files.
2. Compares the open file paths of each process against a list of monitored files.
3. Logs details of processes holding locks on the monitored files to a log file and optionally prints them to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Define the list of files to monitor in the script:
   ```python
   MONITORED_FILES = ["/etc/passwd", "/var/log/syslog", "C:\\Windows\\System32\\config\\SAM"]
   ```

3. Run the script:
   ```bash
   python log_file_locking_processes.py
   ```

4. Check the log file for details of processes holding file locks:
   ```bash
   cat file_locking_processes_log.txt
   ```

## Configuration

- **Monitored Files**: Update the `MONITORED_FILES` list to include files of interest.
- **Log File**: Logs are saved to `file_locking_processes_log.txt` by default. Update the `log_file` variable to use a different file name or path.
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).

## Example Log File

When a process is detected holding a lock on a monitored file, a log entry like the following is saved in the log file:

```
File Locking Processes Log - 2024-12-23 01:00:00
============================================================
[2024-12-23 01:00:05] File Lock Detected - PID: 1234, Name: python, File: /etc/passwd
[2024-12-23 01:00:10] File Lock Detected - PID: 5678, Name: syslogd, File: /var/log/syslog
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain process and file details.
- Processes that open and close files quickly may not be detected if the polling interval is too long.

## Limitations

- The script checks for open files, but it does not directly determine if a file is locked. For explicit file locking, additional tools or system calls may be needed.
- File paths must exactly match the entries in the `MONITORED_FILES` list for detection.

## Author

**Ronald Baker**  
A developer focused on creating tools for system monitoring and file security.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Monitor and secure critical file usage effectively! 📂🔒
```
