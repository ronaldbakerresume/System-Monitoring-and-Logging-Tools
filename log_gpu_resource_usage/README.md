```markdown
# log_gpu_resource_usage.py

A Python script that monitors and logs processes consuming GPU resources. This tool is particularly useful for systems with NVIDIA GPUs to track GPU memory usage and identify resource-intensive applications.

## Features

- **GPU Resource Tracking**: Monitors processes using NVIDIA GPUs and logs their PID, name, and memory usage.
- **Real-Time Monitoring**: Logs GPU usage in real-time with timestamps.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS (requires NVIDIA GPUs and drivers).

## How It Works

1. The script uses the `nvidia-smi` command to query GPU resource usage.
2. Parses the output to extract details about GPU processes, including PID, process name, and GPU memory usage.
3. Logs the extracted details to a file and optionally prints them to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **NVIDIA Drivers**:
  - The `nvidia-smi` command must be available (requires NVIDIA GPUs and drivers).

## Usage

1. Ensure that NVIDIA drivers are installed, and `nvidia-smi` is available in your system's PATH:
   ```bash
   nvidia-smi
   ```

2. Run the script:
   ```bash
   python log_gpu_resource_usage.py
   ```

3. Check the log file for GPU resource usage details:
   ```bash
   cat gpu_resource_usage_log.txt
   ```

## Configuration

- **Polling Interval**: The script polls every 5 seconds by default. Update the `time.sleep(5)` line to adjust the interval.
- **Log File**: Logs are saved to `gpu_resource_usage_log.txt` by default. Update the `log_file` variable in the script to use a different file name or path.

## Example Log File

When processes are detected using GPU resources, a log entry like the following is saved in the log file:

```
GPU Resource Usage Log - 2024-12-23 00:30:00
============================================================
[2024-12-23 00:30:05] GPU Process - PID: 1234, Name: python, Memory Usage: 1024 MiB
[2024-12-23 00:30:10] GPU Process - PID: 5678, Name: chrome, Memory Usage: 512 MiB
```

## Notes

- **Permission Requirements**:
  - Elevated permissions are not typically required, but ensure that the user has access to the `nvidia-smi` command.
- **Hardware and Driver Dependency**:
  - This script requires NVIDIA GPUs and installed drivers. It will not work on systems without compatible hardware.

## Limitations

- The script depends on the availability of the `nvidia-smi` command. If it is not installed or not found, the script will not run.
- Rapidly fluctuating GPU usage may not be captured effectively if the polling interval is too long.

## Author

**Ronald Baker**  
A developer focused on creating tools for monitoring hardware and optimizing system resources.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Monitor GPU resource usage effectively! 🖥️🎮
```