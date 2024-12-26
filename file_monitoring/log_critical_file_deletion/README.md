# log_critical_file_deletion.py

A Python script that monitors and logs attempts to delete critical system files. This tool is essential for detecting unauthorized or accidental deletion of key system files that may compromise system integrity.

## Features

- **Critical File Monitoring**: Tracks a predefined list of critical system files for deletion attempts.
- **Real-Time Logging**: Logs deletion and restoration events for monitored files with timestamps.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.

## How It Works

1. The script maintains an initial state of monitored critical files.
2. Periodically checks the existence of these files.
3. Logs deletion and restoration events to a file and optionally prints them to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - Built-in libraries (`os`, `psutil`, `time`, `datetime`) are sufficient.

## Usage

1. Define the critical files to monitor in the script:
   ```python
   CRITICAL_FILES = ["/etc/passwd", "/etc/hosts", "/etc/sudoers", "C:\\Windows\\System32\\drivers\\etc\\hosts"]
   ```

2. Run the script:
   ```bash
   python log_critical_file_deletion.py
   ```

3. Check the log file for deletion attempts:
   ```bash
   cat critical_file_deletion_log.txt
   ```

## Configuration

- **Critical Files**: Update the `CRITICAL_FILES` list to include the paths of files you wish to monitor.
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `critical_file_deletion_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

When a critical file is deleted or restored, entries like the following are saved in the log file:

```
Critical File Deletion Log - 2024-12-23 02:30:00
============================================================
[2024-12-23 02:30:05] Critical File Deleted: /etc/passwd
[2024-12-23 02:35:10] Critical File Restored: /etc/passwd
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain file paths, especially on Windows and Linux.
- **File Restoration Logs**:
  - The script optionally logs when a deleted file reappears (restored or recreated).

## Limitations

- The script monitors the existence of files but does not detect the process responsible for deletion. Additional tools or system logging mechanisms may be required for detailed attribution.
- Files that are quickly deleted and recreated between polling intervals may not be logged accurately.

## Author

**Ronald Baker**  
A developer focused on creating tools for monitoring critical system activities.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Secure critical system files effectively! 🔒
```
