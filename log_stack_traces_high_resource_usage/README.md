
# log_stack_traces_high_resource_usage.py

A Python script that captures and logs stack traces of processes consuming excessive resources (CPU or memory). This tool is ideal for diagnosing performance bottlenecks and identifying resource-intensive processes.

## Features

- **Resource Monitoring**: Tracks CPU and memory usage of all running processes.
- **Threshold-Based Logging**: Captures stack traces for processes exceeding customizable CPU or memory thresholds.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.
- **Detailed Logging**: Logs process details (PID, name, CPU, memory) along with stack traces.

## How It Works

1. The script uses the `psutil` library to monitor all running processes for resource usage.
2. Processes exceeding the specified CPU or memory usage thresholds are flagged.
3. For each flagged process, the script attempts to capture its stack trace and logs the information to a file.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Configure the resource usage thresholds in the script:
   ```python
   CPU_THRESHOLD = 50.0  # CPU usage percentage
   MEMORY_THRESHOLD_MB = 500  # Memory usage in MB
   ```

3. Run the script:
   ```bash
   python log_stack_traces_high_resource_usage.py
   ```

4. Check the log file for stack traces of flagged processes:
   ```bash
   cat high_resource_usage_stack_traces_log.txt
   ```

## Configuration

- **Thresholds**: Update the `CPU_THRESHOLD` and `MEMORY_THRESHOLD_MB` variables to adjust the thresholds for high resource usage.
- **Log File**: Logs are saved to `high_resource_usage_stack_traces_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

An example log entry might look like:

```
High Resource Usage Stack Trace Log - 2024-12-22 20:00:00
============================================================
[2024-12-22 20:00:05] High Resource Usage Process - PID: 1234, Name: chrome, CPU: 75.32%, Memory: 1024.56 MB
Stack Trace for PID 1234:
  File "/usr/lib/python3.8/threading.py", line 890, in _bootstrap
    self._bootstrap_inner()
  File "/usr/lib/python3.8/threading.py", line 932, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.8/threading.py", line 870, in run
    self._target(*self._args, **self._kwargs)
...
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain process information or stack traces.
- Processes that terminate quickly or are inaccessible during monitoring are automatically skipped.
- The script runs a single iteration by default. To run it periodically, consider wrapping it in a loop or using a task scheduler (e.g., `cron` on Linux or Task Scheduler on Windows).

## Author

**Ronald Baker**  
A developer focused on creating tools for diagnosing system performance and enhancing resource monitoring.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Diagnose and optimize your system efficiently! 🛠️
```
