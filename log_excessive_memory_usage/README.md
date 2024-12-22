```markdown
# log_excessive_memory_usage.py

A Python script that monitors and logs processes consuming excessive memory over time. This tool is useful for identifying memory-intensive applications that may be impacting system performance.

## Features

- **Memory Usage Tracking**: Detects processes consuming memory above a specified threshold.
- **Real-Time Logging**: Logs process details (PID, name, and memory usage) with timestamps.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.

## How It Works

1. The script uses the `psutil` library to monitor running processes in real-time.
2. Evaluates the Resident Set Size (RSS) memory usage for each process.
3. Logs details of processes exceeding the defined memory threshold to a file and optionally prints them to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Configure the memory usage threshold in the script:
   ```python
   MEMORY_USAGE_THRESHOLD_MB = 500  # Memory usage in MB
   ```

3. Run the script:
   ```bash
   python log_excessive_memory_usage.py
   ```

4. Check the log file for excessive memory usage details:
   ```bash
   cat excessive_memory_usage_log.txt
   ```

## Configuration

- **Threshold**: Update the `MEMORY_USAGE_THRESHOLD_MB` variable to adjust the threshold for excessive memory usage (default: 500 MB).
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `excessive_memory_usage_log.txt` by default. Update the `log_file` variable in the script to use a different file name or path.

## Example Log File

When a process exceeds the memory usage threshold, a log entry like the following is saved in the log file:

```
Excessive Memory Usage Log - 2024-12-23 01:15:00
============================================================
[2024-12-23 01:15:05] Excessive Memory Usage Detected - PID: 1234, Name: chrome, Memory Usage: 1024.50 MB
[2024-12-23 01:15:10] Excessive Memory Usage Detected - PID: 5678, Name: python, Memory Usage: 768.25 MB
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain process details.
- Processes with fluctuating memory usage may exceed the threshold temporarily and appear in the logs.

## Limitations

- The script evaluates memory usage in real-time. Short-lived spikes in memory usage may not be consistently captured if the polling interval is too long.
- Memory usage thresholds should be adjusted based on the system's overall resources and expected application behavior.

## Author

**Ronald Baker**  
A developer focused on creating tools for monitoring and optimizing system performance.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Monitor and manage excessive memory usage effectively! 💾
```