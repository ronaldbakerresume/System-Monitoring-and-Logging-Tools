import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Threshold for excessive open file descriptors
FILE_DESCRIPTOR_THRESHOLD = 100  # Example: More than 100 open files

# Output file to save the log of excessive file descriptor usage
log_file = "excessive_file_descriptors_log.txt"

def log_excessive_file_descriptors(duration_seconds=30, polling_interval=5):
    """
    Monitors and logs processes with excessive file descriptors.

    Args:
        duration_seconds (int): The duration to monitor in seconds (default is 30).
        polling_interval (int): The interval to poll processes in seconds (default is 5).

    Returns:
        str: A string output of the log for testing purposes.
    """
    start_time = time.time()
    log_output = []

    with open(log_file, "a") as file:
        file.write(f"Excessive File Descriptors Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("=" * 60 + "\n")

        try:
            while time.time() - start_time < duration_seconds:
                # Iterate through all running processes
                for process in psutil.process_iter(attrs=["pid", "name"]):
                    try:
                        # Get process details
                        pid = process.info["pid"]
                        name = process.info["name"]

                        # Get the number of open file descriptors
                        num_fds = len(process.open_files())

                        # Check if the process exceeds the threshold
                        if num_fds > FILE_DESCRIPTOR_THRESHOLD:
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            log_entry = (f"[{timestamp}] Excessive File Descriptors Detected - "
                                         f"PID: {pid}, Name: {name}, Open File Descriptors: {num_fds}\n")
                            file.write(log_entry)
                            log_output.append(log_entry.strip())
                            print(log_entry.strip())  # Print to the console

                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        # Skip processes that are inaccessible or have terminated
                        continue

                time.sleep(polling_interval)  # Poll at specified intervals

        except KeyboardInterrupt:
            print("Monitoring stopped. Excessive file descriptors log saved.")

    return "\n".join(log_output)


if __name__ == "__main__":
    log_excessive_file_descriptors()

