import psutil  # For process and connection monitoring
from datetime import datetime  # To timestamp the log file
import time  # For timed polling

def log_hardware_interactions(duration_seconds=30, log_file="hardware_interactions_log.txt"):
    """
    Monitors and logs processes interacting with hardware devices like USB and network interfaces.

    Args:
        duration_seconds (int): Duration to monitor in seconds (default is 30).
        log_file (str): Path to the log file (default is "hardware_interactions_log.txt").

    Returns:
        str: String of log entries for testing purposes.
    """
    start_time = time.time()
    log_output = []

    with open(log_file, "a") as file:
        file.write(f"Hardware Interactions Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("=" * 60 + "\n")

        try:
            while time.time() - start_time < duration_seconds:
                # Iterate through all network connections
                for conn in psutil.net_connections(kind="inet"):
                    try:
                        # Get connection details
                        pid = conn.pid
                        local_address = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                        remote_address = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                        status = conn.status

                        # Get the process associated with the connection
                        if pid:
                            process = psutil.Process(pid)
                            name = process.name()

                            # Log the connection and process details
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            log_entry = (f"[{timestamp}] Process: PID {pid}, Name: {name}, "
                                         f"Local Address: {local_address}, Remote Address: {remote_address}, "
                                         f"Status: {status}\n")
                            file.write(log_entry)
                            log_output.append(log_entry.strip())
                            print(log_entry.strip())  # Print to the console

                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        # Skip processes that are inaccessible or have terminated
                        continue

                time.sleep(5)  # Poll every 5 seconds

        except Exception as e:
            error_msg = f"An error occurred: {e}\n"
            print(error_msg)
            file.write(error_msg)

    return "\n".join(log_output)


if __name__ == "__main__":
    log_hardware_interactions()

