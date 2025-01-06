import psutil  # For process monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

def log_low_cpu_usage_processes(duration_seconds=30, polling_interval=5, log_file="low_cpu_usage_log.txt"):
    """
    Monitors and logs processes with unusually low CPU usage over a specified time period.

    Args:
        duration_seconds (int): Total time to monitor in seconds (default is 30 seconds).
        polling_interval (int): Time between polls in seconds (default is 5 seconds).
        log_file (str): Path to the log file (default is "low_cpu_usage_log.txt").

    Returns:
        str: String of log entries for testing and review purposes.
    """
    start_time = time.time()
    log_output = []

    with open(log_file, "a") as file:
        file.write(f"Low CPU Usage Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("=" * 60 + "\n")

        try:
            while time.time() - start_time < duration_seconds:
                # Iterate through all running processes
                for process in psutil.process_iter(attrs=["pid", "name", "cpu_percent"]):
                    try:
                        # Get process details
                        pid = process.info["pid"]
                        name = process.info["name"]
                        cpu_usage = process.info["cpu_percent"]

                        # Check if the CPU usage is below the threshold
                        if cpu_usage < LOW_CPU_USAGE_THRESHOLD:
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            log_entry = (f"[{timestamp}] Low CPU Usage Detected - "
                                         f"PID: {pid}, Name: {name}, CPU Usage: {cpu_usage:.2f}%\n")
                            file.write(log_entry)
                            log_output.append(log_entry.strip())
                            print(log_entry.strip())  # Print to the console

                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        # Skip processes that are inaccessible or have terminated
                        continue

                time.sleep(polling_interval)

        except Exception as e:
            error_msg = f"An error occurred: {e}\n"
            print(error_msg)
            file.write(error_msg)

    return "\n".join(log_output)


if __name__ == "__main__":
    LOW_CPU_USAGE_THRESHOLD = 1.0  # Example threshold: Less than 1% CPU usage
    log_low_cpu_usage_processes(duration_seconds=30, polling_interval=5)

