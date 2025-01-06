import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Threshold for excessive child processes
CHILD_PROCESS_THRESHOLD = 10  # Example: More than 10 child processes

def log_excessive_child_processes(duration_seconds=60, polling_interval=5):
    """
    Monitors and logs processes spawning excessive child processes for a specified duration.

    Args:
        duration_seconds (int): Duration for monitoring in seconds.
        polling_interval (int): Interval for polling in seconds.

    Returns:
        str: A string containing the log of excessive child processes detected.
    """
    log_output = []  # Store log entries as a list of strings
    start_time = time.time()

    log_output.append(f"Excessive Child Processes Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_output.append("=" * 60)

    try:
        while time.time() - start_time < duration_seconds:
            # Iterate through all running processes
            for process in psutil.process_iter(attrs=["pid", "name"]):
                try:
                    # Get process details
                    pid = process.info["pid"]
                    name = process.info["name"]

                    # Get the child processes of the current process
                    child_processes = process.children(recursive=True)

                    # Check if the number of child processes exceeds the threshold
                    if len(child_processes) > CHILD_PROCESS_THRESHOLD:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_entry = (f"[{timestamp}] Excessive Child Processes Detected - "
                                     f"PID: {pid}, Name: {name}, Child Process Count: {len(child_processes)}")
                        log_output.append(log_entry)
                        print(log_entry)  # Print to the console

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # Skip processes that are inaccessible or have terminated
                    continue

            time.sleep(polling_interval)  # Poll at the specified interval

    except KeyboardInterrupt:
        log_output.append("Monitoring stopped by user.")

    log_output.append("Monitoring completed.")
    return "\n".join(log_output)

# Example usage
if __name__ == "__main__":
    duration = 30  # Run for 30 seconds
    output = log_excessive_child_processes(duration_seconds=duration)
    with open("excessive_child_processes_log_output.txt", "w") as file:
        file.write(output)
    print("Log saved to excessive_child_processes_log_output.txt")
