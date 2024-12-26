
# log_privilege_escalation_attempts.py

A Python script that monitors and logs unauthorized attempts to escalate privileges via processes. This tool is essential for detecting potential security threats and malicious activity on a system.

## Features

- **Privilege Escalation Detection**: Identifies processes attempting to use known privilege escalation commands.
- **Real-Time Monitoring**: Continuously scans running processes for suspicious commands.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.
- **Detailed Logging**: Logs process details (PID, name, command, and user) with timestamps.

## How It Works

1. The script uses the `psutil` library to monitor running processes in real time.
2. It checks process command lines against a predefined list of known privilege escalation commands (e.g., `sudo`, `su`, `pkexec`).
3. If a match is found, the process details are logged to a file and printed to the console.

## Requirements

- **Python**: Version 3.6 or newer
- **Dependencies**:
  - `psutil` library (install via `pip install psutil`)

## Usage

1. Install the required dependencies:
   ```bash
   pip install psutil
   ```

2. Define the list of known privilege escalation commands in the script:
   ```python
   ESCALATION_COMMANDS = ["sudo", "su", "setuid", "pkexec", "runas"]
   ```

3. Run the script:
   ```bash
   python log_privilege_escalation_attempts.py
   ```

4. Check the log file for detected privilege escalation attempts:
   ```bash
   cat privilege_escalation_attempts_log.txt
   ```

## Configuration

- **Escalation Commands**: Update the `ESCALATION_COMMANDS` list to include additional commands or processes of interest.
- **Polling Interval**: Adjust the `time.sleep(5)` line to change the monitoring frequency (default: 5 seconds).
- **Log File**: Logs are saved to `privilege_escalation_attempts_log.txt` by default. Update the `log_file` variable to use a different file name or path.

## Example Log File

When a privilege escalation attempt is detected, a log entry like the following is saved in the log file:

```
Privilege Escalation Attempts Log - 2024-12-22 22:30:00
============================================================
[2024-12-22 22:30:05] Privilege Escalation Detected - PID: 1234, Name: bash, User: john, Command: sudo apt update
[2024-12-22 22:30:10] Privilege Escalation Detected - PID: 5678, Name: pkexec, User: jane, Command: pkexec some_application
```

## Notes

- **Permission Requirements**:
  - Elevated permissions may be required to access certain process information.
- Processes that terminate quickly may not appear in the log if they execute within the polling interval.

## Limitations

- The script identifies potential privilege escalation attempts based on predefined commands. Custom or obfuscated commands may not be detected.
- Rapid execution and termination of processes may result in missed detections.

## Author

**Ronald Baker**  
A developer dedicated to enhancing system security and monitoring tools.

## License

This script is licensed under the [MIT License](LICENSE), permitting free use, modification, and distribution.

---

Stay vigilant and secure your system from privilege escalation attempts! 🔒
```
