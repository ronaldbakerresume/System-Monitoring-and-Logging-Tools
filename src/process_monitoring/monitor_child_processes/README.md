
# monitor_child_processes.py

A Python script that monitors child processes spawned by a specific parent process and logs their details. This tool is ideal for tracking subprocesses created by critical applications or services.

## Features

- **Targeted Monitoring**: Tracks child processes of a specific parent process using its PID.
- **Real-Time Logging**: Captures child process details, including PID, name, and command-line arguments.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.

## How It Works

1. The script uses the `psutil` library to monitor a specific parent process by its PID.
2. It retrieves all child processes spawned by the parent process, including recursively spawned children.
3. New child processes are logged to a file and printed to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Specify the PID of the parent process to monitor:
   ```python
   parent_pid = 1234  # Replace with the actual PID of the parent process
   ```

3. Run the script:
   ```bash
   python monitor_child_processes.py
   ```

4. To stop monitoring, press `Ctrl+C`. The script will save all logged data to the log file.

## Configuration

- **Parent Process**: Update the `parent_pid` variable in the script to the PID of the process you want to monitor.
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `child_processes_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

When a new child process is detected, a log entry like the following is saved in the log file:

```
Child Process Log - 2024-12-22 18:00:00
============================================================
[2024-12-22 18:00:05] Child PID: 5678, Name: python, Command: python child_script.py
[2024-12-22 18:00:10] Child PID: 9101, Name: bash, Command: bash -c "some_command"
```

## Notes

- **Parent Process Monitoring**:
  - The parent process must be running for the script to detect child processes. If the parent process terminates, the script will stop detecting children.
- **Permission Requirements**:
  - Elevated permissions may be required to access certain process information.
- **Duplicate Logging Prevention**:
  - The script keeps track of already logged child PIDs to avoid duplicate entries.

## Author

**Ronald Baker**  
A developer dedicated to creating tools for process monitoring and system optimization.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Stay informed about subprocess activity! 🛠️
```
