import psutil  # For system process monitoring
from datetime import datetime  # To timestamp the log file


def log_process_hierarchy(log_file="process_hierarchy_log.txt"):
    """
    Logs parent-child relationships for all active processes.

    Args:
        log_file (str): Path to the log file (default is "process_hierarchy_log.txt").

    Returns:
        str: Text output of the process hierarchy log.
    """
    log_output = []
    header = f"Process Hierarchy Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n" + "=" * 60 + "\n"
    log_output.append(header)

    try:
        # Iterate through all running processes
        for process in psutil.process_iter(attrs=["pid", "name", "ppid"]):
            try:
                # Get process details
                pid = process.info["pid"]
                name = process.info["name"]
                ppid = process.info["ppid"]

                # Try to get the parent process details
                try:
                    parent = psutil.Process(ppid)
                    parent_name = parent.name()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    parent_name = "N/A"

                # Log the process hierarchy
                log_entry = (f"Process: PID {pid}, Name: {name} --> "
                             f"Parent: PID {ppid}, Name: {parent_name}")
                log_output.append(log_entry)

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Skip processes that are inaccessible or have terminated
                continue

    except Exception as e:
        error_msg = f"An error occurred: {e}"
        log_output.append(error_msg)

    # Save the log to a file
    with open(log_file, "w") as file:
        file.write("\n".join(log_output))

    # Return the log as a text string
    return "\n".join(log_output)


if __name__ == "__main__":
    output = log_process_hierarchy()
    print(output)  # Print the log for immediate feedback

