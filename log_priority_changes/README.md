
# log_priority_changes.py

A Python script that tracks and logs scheduling priority changes for running processes. This tool is useful for monitoring process behavior and detecting unexpected priority adjustments that may affect system performance.

## Features

- **Priority Change Detection**: Monitors changes in scheduling priority (`nice` value) for all running processes.
- **Real-Time Logging**: Logs process details (PID, name, old priority, and new priority) with timestamps.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.

## How It Works

1. The script uses the `psutil` library to monitor running processes in real time.
2. It maintains a dictionary to track the last known priority (`nice` value) of each process.
3. Any change in a process's priority is logged to a file and optionally printed to the console.

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
   python log_priority_changes.py
   ```

3. Check the log file for priority changes:
   ```bash
   cat priority_changes_log.txt
   ```

## Configuration

- **Log File**: Logs are saved to `priority_changes_log.txt` by default. Update the `log_file` variable in the script to use a different file name or path.
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).

## Example Log File

When a priority change is detected, a log entry like the following is saved in the log file:

```
Process Priority Changes Log - 2024-12-22 22:45:00
============================================================
[2024-12-22 22:45:05] Priority Change Detected - PID: 1234, Name: python, Old Priority: 0, New Priority: 10
[2024-12-22 22:45:10] Priority Change Detected - PID: 5678, Name: chrome, Old Priority: 5, New Priority: -5
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain process details or priority changes.
- Processes that terminate quickly may not appear in the log if they exit before their priority change is detected.

## Limitations

- The script tracks only processes visible at the time of execution. New processes are tracked when detected, but terminated processes are removed from the tracking dictionary.

## Author

**Ronald Baker**  
A developer focused on creating tools for process monitoring and system optimization.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Monitor and understand priority changes in your system processes effectively! 🛠️
```
