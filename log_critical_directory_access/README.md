```markdown
# log_critical_directory_access.py

A Python script that monitors processes accessing critical directories (e.g., `/etc`, `/home`) and logs their details. This tool is useful for detecting unauthorized or unexpected access to sensitive system directories.

## Features

- **Critical Directory Monitoring**: Tracks access to specified critical directories by processes.
- **Real-Time Logging**: Logs process details (PID, name, and accessed path) with timestamps.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.

## How It Works

1. The script uses the `psutil` library to monitor processes and their open files.
2. Checks if open files accessed by processes are located within specified critical directories.
3. Logs details of these processes to a file and optionally prints them to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Define the critical directories to monitor in the script:
   ```python
   CRITICAL_DIRECTORIES = ["/etc", "/home", "C:\\Windows\\System32", "/var"]
   ```

3. Run the script:
   ```bash
   python log_critical_directory_access.py
   ```

4. Check the log file for directory access details:
   ```bash
   cat critical_directory_access_log.txt
   ```

## Configuration

- **Critical Directories**: Update the `CRITICAL_DIRECTORIES` list to include the directories you wish to monitor.
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `critical_directory_access_log.txt` by default. Update the `log_file` variable in the script to use a different file name or path.

## Example Log File

When a process accesses a critical directory, entries like the following are saved in the log file:

```
Critical Directory Access Log - 2024-12-23 02:45:00
============================================================
[2024-12-23 02:45:05] Process: PID 1234, Name: python, Accessed Path: /etc/passwd
[2024-12-23 02:45:10] Process: PID 5678, Name: nginx, Accessed Path: /var/log/nginx/access.log
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain file and process details.
- Processes accessing files outside the listed critical directories will not be logged.

## Limitations

- The script detects file accesses based on currently open files. Rapid file access and closure may not be captured if the polling interval is too long.
- On Windows, long paths or permission-restricted directories may cause some processes to be skipped.

## Author

**Ronald Baker**  
A developer focused on creating tools for monitoring and securing system activities.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Monitor and secure critical directory access effectively! 📂
```