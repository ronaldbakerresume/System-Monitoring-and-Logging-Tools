```markdown
# log_process_hierarchy.py

A Python script that logs parent-child relationships for all active processes. This tool provides insight into the process hierarchy, helping to identify how processes are spawned and organized.

## Features

- **Process Hierarchy**: Captures and logs parent-child relationships for all active processes.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.
- **Detailed Logging**: Logs process details (PID, name, parent PID, and parent name) with timestamps.

## How It Works

1. The script uses the `psutil` library to access information about all running processes.
2. For each process, it identifies the parent process and logs their relationship.
3. Details are written to a log file and optionally printed to the console.

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
   python log_process_hierarchy.py
   ```

3. Check the log file for the captured process hierarchy:
   ```bash
   cat process_hierarchy_log.txt
   ```

## Configuration

- **Log File**: Logs are saved to `process_hierarchy_log.txt` by default. Update the `log_file` variable in the script to use a different file name or path.

## Example Log File

A sample log file might look like:

```
Process Hierarchy Log - 2024-12-22 21:30:00
============================================================
Process: PID 1, Name: systemd --> Parent: PID 0, Name: N/A
Process: PID 234, Name: bash --> Parent: PID 1, Name: systemd
Process: PID 567, Name: python --> Parent: PID 234, Name: bash
...
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain process details.
- Processes that terminate quickly or are inaccessible during monitoring may not appear in the log.
- The script captures a snapshot of the process hierarchy at the time of execution.

## Author

**Ronald Baker**  
A developer committed to creating tools for process monitoring and system analysis.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Analyze your process hierarchy with ease! 🖥️
```