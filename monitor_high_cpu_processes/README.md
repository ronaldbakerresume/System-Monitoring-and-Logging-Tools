
# monitor_high_cpu_processes.py

A Python script designed to monitor processes with high CPU usage and log their details to a file. This tool is useful for detecting and analyzing resource-intensive processes on a system.

## Features

- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.
- **Real-Time Monitoring**: Captures processes exceeding a customizable CPU usage threshold.
- **Detailed Logging**: Logs process details (PID, name, CPU usage, and command line) to a timestamped file.

## How It Works

1. The script executes a system command (`ps` on Linux/macOS or `wmic` on Windows) to gather process information.
2. It parses the output to identify processes exceeding a specified CPU usage threshold.
3. The details of these processes are logged to a file for further analysis.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - None (uses built-in Python libraries)

## Usage

1. Configure the CPU usage threshold in the script:
   ```python
   CPU_THRESHOLD = 10.0  # Percentage of CPU usage
   ```

2. Run the script:
   ```bash
   python monitor_high_cpu_processes.py
   ```

3. The script will log high CPU usage processes to `high_cpu_processes_log.txt`.

## Configuration

- **Threshold**: Modify the `CPU_THRESHOLD` variable in the script to change the minimum CPU usage required to log a process.
- **Log File**: Logs are saved to `high_cpu_processes_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

An example log entry might look like:

```
High CPU Process Log - 2024-12-22 12:00:00
============================================================
PID: 1234, Name: chrome, CPU: 25.6%, Command: /usr/bin/chrome --type=renderer
PID: 5678, Name: python, CPU: 15.2%, Command: python my_script.py
```

## Notes

- The script adjusts the system command based on the operating system:
  - Linux/MacOS: Uses the `ps` command.
  - Windows: Uses the `wmic` command.
- Processes that do not conform to the expected output format are skipped.
- The script runs once and logs all matching processes at the time of execution. For continuous monitoring, you can implement a loop or schedule the script.

## Author

**Ronald Baker**  
A developer passionate about building tools for system monitoring and performance optimization.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Optimize wisely! 🚀
```
