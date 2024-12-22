```markdown
# log_unauthorized_execution.py

A Python script that monitors and logs processes executing from unauthorized directories. This tool is helpful for detecting potentially malicious or unauthorized software execution on a system.

## Features

- **Real-Time Monitoring**: Continuously checks running processes for unauthorized execution paths.
- **Customizable Authorization**: Specify directories that are authorized for process execution.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.
- **Detailed Logging**: Logs unauthorized executions with process details (PID, name, and executable path).

## How It Works

1. The script uses the `psutil` library to monitor the executable paths of all running processes.
2. It checks whether the executable path of each process starts with any directory in the authorized list.
3. If a process executes from an unauthorized path, its details are logged to a file and printed to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Define the list of authorized directories in the script:
   ```python
   AUTHORIZED_DIRECTORIES = ["/usr/bin", "/bin", "C:\\Windows\\System32", "/usr/sbin"]
   ```

3. Run the script:
   ```bash
   python log_unauthorized_execution.py
   ```

4. To stop monitoring, press `Ctrl+C`. The script will save all logged data to the log file.

## Configuration

- **Authorized Directories**: Update the `AUTHORIZED_DIRECTORIES` list to specify the paths where execution is allowed.
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `unauthorized_execution_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

When an unauthorized execution is detected, a log entry like the following is saved in the log file:

```
Unauthorized Execution Log - 2024-12-22 18:30:00
============================================================
[2024-12-22 18:30:05] Unauthorized Execution Detected - PID: 1234, Name: malware.exe, Executable Path: /home/user/malware.exe
[2024-12-22 18:30:10] Unauthorized Execution Detected - PID: 5678, Name: unknown_script.sh, Executable Path: /tmp/unknown_script.sh
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain process information.
- Processes that terminate quickly or are inaccessible during monitoring are automatically skipped.
- The script runs in a continuous loop for real-time monitoring. To run it periodically, consider scheduling it using a task scheduler (e.g., `cron` on Linux or Task Scheduler on Windows).

## Author

**Ronald Baker**  
A developer focused on creating tools to enhance system security and ensure compliance with execution policies.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Secure your system against unauthorized executions! 🔒
```