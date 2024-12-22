```markdown
# monitor_network_traffic.py

A Python script to monitor processes that generate significant network traffic. It logs details about processes that exceed predefined thresholds for sent and received data. This tool is useful for administrators and developers to detect unusual or high network activity.

## Features

- **Real-Time Monitoring**: Continuously tracks processes' network activity.
- **Customizable Thresholds**: Easily configure thresholds for sent and received data.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.
- **Logging**: Saves details of high network traffic processes to a timestamped log file.
- **Console Output**: Provides real-time updates of flagged processes.

## How It Works

1. The script uses the `psutil` library to track processes' network connections and I/O statistics.
2. It calculates the difference in network usage over a polling interval.
3. If a process exceeds the defined thresholds for sent or received data, it logs the details (PID, name, and traffic statistics) to a file and prints them to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Configure thresholds in the script:
   ```python
   SENT_THRESHOLD = 1024 * 1024  # Threshold for sent data (1 MB/s)
   RECEIVED_THRESHOLD = 1024 * 1024  # Threshold for received data (1 MB/s)
   ```

3. Run the script:
   ```bash
   python monitor_network_traffic.py
   ```

4. To stop monitoring, press `Ctrl+C`. The script will save all logged data to the log file.

## Configuration

- **Thresholds**: Modify the `SENT_THRESHOLD` and `RECEIVED_THRESHOLD` variables in the script to adjust the network traffic limits.
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `high_network_traffic_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

When a process exceeds the traffic thresholds, a log entry like the following is saved in the log file:

```
High Network Traffic Log - 2024-12-22 11:00:00
============================================================
[2024-12-22 11:00:05] High Network Traffic - PID: 1234, Name: chrome, Sent: 1500000 bytes, Received: 1200000 bytes
[2024-12-22 11:00:10] High Network Traffic - PID: 5678, Name: python, Sent: 2000000 bytes, Received: 1800000 bytes
```

## Notes

- Processes that terminate or are inaccessible during monitoring (due to permissions) are automatically skipped.
- Network traffic is measured in bytes, and thresholds are configurable to suit specific requirements.

## Author

**Ronald Baker**  
A developer dedicated to creating efficient tools for network monitoring and system optimization.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Happy monitoring! 🌐
```