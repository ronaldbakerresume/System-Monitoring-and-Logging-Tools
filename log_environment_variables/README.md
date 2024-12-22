
# log_environment_variables.py

A Python script that captures and logs the environment variables of specific processes. This tool is useful for debugging, monitoring, and auditing processes with critical or sensitive configurations.

## Features

- **Environment Variable Monitoring**: Captures and logs the environment variables of specified processes.
- **Real-Time Logging**: Logs process details (PID, name, and environment variables) with timestamps.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.

## How It Works

1. The script uses the `psutil` library to monitor running processes.
2. Checks the environment variables of processes matching a predefined list of monitored process names.
3. Logs details of the environment variables for these processes to a file and optionally prints them to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Configure the monitored processes in the script:
   ```python
   MONITORED_PROCESSES = ["nginx", "mysql", "python", "explorer.exe"]
   ```

3. Run the script:
   ```bash
   python log_environment_variables.py
   ```

4. Check the log file for environment variable details:
   ```bash
   cat process_environment_variables_log.txt
   ```

## Configuration

- **Monitored Processes**: Update the `MONITORED_PROCESSES` list to include the names of processes you wish to monitor.
- **Log File**: Logs are saved to `process_environment_variables_log.txt` by default. Update the `log_file` variable in the script to use a different file name or path.

## Example Log File

When environment variables are logged for a monitored process, entries like the following are saved in the log file:

```
Process Environment Variables Log - 2024-12-23 02:00:00
============================================================
[2024-12-23 02:00:05] Process: PID 1234, Name: nginx
  PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin
  HOME=/root
  LANG=en_US.UTF-8

[2024-12-23 02:00:10] Process: PID 5678, Name: python
  PATH=/usr/local/bin:/usr/bin
  PYTHONPATH=/usr/local/lib/python3.9/site-packages
  LANG=en_US.UTF-8
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access environment variables for certain processes.
- Only processes explicitly listed in the `MONITORED_PROCESSES` list are logged.

## Limitations

- The script captures environment variables in real-time. If a process modifies its environment variables after being logged, the updated values will not be captured.
- Processes that terminate quickly may not appear in the log if they exit before detection.

## Author

**Ronald Baker**  
A developer focused on creating tools for monitoring and auditing system resources.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Monitor and analyze process environment variables effectively! 🌍
```
