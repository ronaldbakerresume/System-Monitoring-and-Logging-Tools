```markdown
# monitor_unauthorized_processes.py

A Python script that monitors the system for unauthorized processes and logs their details to a file. This tool is essential for system administrators and security personnel to detect and track processes that are not part of the predefined authorized list.

## Features

- **Real-Time Monitoring**: Continuously monitors all running processes.
- **Customizable Authorization**: Easily define a list of authorized process names.
- **Cross-Platform Compatibility**: Compatible with Linux, Windows, and macOS.
- **Logging**: Saves details of unauthorized processes to a timestamped log file.
- **Console Output**: Provides real-time updates on unauthorized processes.

## How It Works

1. The script uses the `psutil` library to access information about system processes.
2. It checks each running process against a predefined list of authorized processes.
3. If a process is not in the list, its details (PID, name, and command line) are logged to a file and printed to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Define the list of authorized processes in the `AUTHORIZED_PROCESSES` variable within the script. Example:
   ```python
   AUTHORIZED_PROCESSES = [
       "python", "bash", "systemd", "explorer.exe", "chrome", "firefox"
   ]
   ```

3. Run the script:
   ```bash
   python monitor_unauthorized_processes.py
   ```

4. To stop monitoring, press `Ctrl+C`. The script will save all logged data to the log file.

## Configuration

- **Authorized Processes**: Update the `AUTHORIZED_PROCESSES` list to include only the names of processes you trust.
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `unauthorized_processes_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

If an unauthorized process is detected, a log entry like the following is saved in the log file:

```
Unauthorized Process Log - 2024-12-22 11:00:00
============================================================
[2024-12-22 11:00:05] Unauthorized Process - PID: 1234, Name: suspicious_app, Command: /usr/bin/suspicious_app --run
[2024-12-22 11:00:10] Unauthorized Process - PID: 5678, Name: unknown_tool, Command: /usr/bin/unknown_tool --arg
```

## Notes

- Processes that terminate or are inaccessible during monitoring (due to permissions) are automatically skipped.
- Be cautious when defining the `AUTHORIZED_PROCESSES` list to avoid accidentally logging trusted processes.

## Author

**Ronald Baker**  
A developer focused on building tools for system monitoring, security, and process management.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Stay secure! 🛡️
```