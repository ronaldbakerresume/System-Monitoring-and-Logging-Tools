
# detect_runaway_processes.py

A Python script that detects and logs runaway processes exceeding a predefined runtime threshold. This tool is designed to identify processes that may be stuck, misbehaving, or consuming system resources for too long.

## Features

- **Runtime Monitoring**: Tracks the duration of all running processes.
- **Runaway Process Detection**: Logs processes exceeding a specified runtime threshold.
- **Real-Time Logging**: Logs process details (PID, name, and runtime) with timestamps.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.

## How It Works

1. The script uses the `psutil` library to monitor running processes.
2. Calculates the runtime of each process by comparing its creation time with the current time.
3. Logs details of processes exceeding the predefined runtime threshold to a file and optionally prints them to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Configure the runaway process runtime threshold in the script:
   ```python
   RUNAWAY_RUNTIME_THRESHOLD = 3600  # Runtime in seconds (default: 1 hour)
   ```

3. Run the script:
   ```bash
   python detect_runaway_processes.py
   ```

4. Check the log file for runaway process details:
   ```bash
   cat runaway_processes_log.txt
   ```

## Configuration

- **Runtime Threshold**: Update the `RUNAWAY_RUNTIME_THRESHOLD` variable to adjust the threshold for runaway processes (default: 3600 seconds or 1 hour).
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `runaway_processes_log.txt` by default. Update the `log_file` variable in the script to use a different file name or path.

## Example Log File

When a runaway process is detected, a log entry like the following is saved in the log file:

```
Runaway Process Log - 2024-12-23 03:45:00
============================================================
[2024-12-23 03:45:05] Runaway Process Detected - PID: 1234, Name: python, Runtime: 7200.50 seconds
[2024-12-23 03:45:10] Runaway Process Detected - PID: 5678, Name: nginx, Runtime: 5400.30 seconds
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access details of certain processes.
- Processes that terminate between polling intervals will not be logged.

## Limitations

- The script calculates runtime in real-time. Short-lived processes that exceed the threshold and terminate quickly may not be captured.
- Ensure the runtime threshold is configured appropriately to avoid false positives for long-running but legitimate processes.

## Author

**Ronald Baker**  
A developer focused on creating tools for monitoring and optimizing system performance.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Identify and manage runaway processes effectively! 🚀
```
