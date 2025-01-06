import os
import subprocess
from datetime import datetime


def log_running_processes(log_file="running_processes_log.txt"):
    """
    Logs all currently running processes and their metadata (PID, name, command).

    Args:
        log_file (str): Path to the log file (default is "running_processes_log.txt").

    Returns:
        str: Text output of all running processes.
    """
    log_output = []
    header = f"Process Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n" + "=" * 50 + "\n"
    log_output.append(header)

    # Determine the command to list processes based on the operating system
    if os.name == "nt":  # For Windows
        command = ["tasklist"]
    else:  # For Linux and MacOS
        command = ["ps", "-eo", "pid,comm,args"]

    # Execute the command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

    # Append the command output to the log
    log_output.append(result.stdout)

    # Save the log to a file
    with open(log_file, "w") as file:
        file.write("\n".join(log_output))

    # Return the log as a text string
    return "\n".join(log_output)


if __name__ == "__main__":
    output = log_running_processes()
    print(output)  # Print the log for immediate feedback


