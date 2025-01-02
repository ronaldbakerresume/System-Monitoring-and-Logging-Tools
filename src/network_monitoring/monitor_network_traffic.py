import psutil  # For process and network monitoring
from datetime import datetime  # To timestamp the log file
import time  # For periodic polling

# Thresholds for network traffic (in bytes per second)
SENT_THRESHOLD = 1024 * 1024  # Example: 1 MB/s
RECEIVED_THRESHOLD = 1024 * 1024  # Example: 1 MB/s

# Function to calculate network traffic for each process
def get_process_network_traffic():
    """
    Returns a dictionary mapping PID to (sent_bytes, received_bytes) for all active processes.
    """
    process_traffic = {}
    for conn in psutil.net_connections(kind="inet"):
        try:
            pid = conn.pid
            if pid is not None and pid in psutil.pids():
                process = psutil.Process(pid)
                if process not in process_traffic:
                    io_counters = process.io_counters()
                    process_traffic[pid] = (io_counters.other_bytes_sent, io_counters.other_bytes_recv)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return process_traffic

# Function to monitor network traffic and log high traffic processes
def monitor_network_traffic(timeout=5):
    """
    Monitors processes sending and receiving large amounts of network traffic for a specified time.
    
    :param timeout: Duration to monitor in seconds (default is 5 seconds)
    :return: A string containing the log of high network traffic processes.
    """
    # Initialize a snapshot of previous network traffic
    previous_traffic = get_process_network_traffic()

    log_entries = []
    log_entries.append(f"High Network Traffic Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_entries.append("=" * 60)

    start_time = time.time()
    
    while time.time() - start_time < timeout:
        # Capture the current network traffic
        current_traffic = get_process_network_traffic()

        for pid, (sent, received) in current_traffic.items():
            try:
                # Calculate the difference in traffic
                prev_sent, prev_received = previous_traffic.get(pid, (0, 0))
                sent_delta = sent - prev_sent
                received_delta = received - prev_received

                # Check if the traffic exceeds the thresholds
                if sent_delta > SENT_THRESHOLD or received_delta > RECEIVED_THRESHOLD:
                    process = psutil.Process(pid)
                    name = process.name()
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = (f"[{timestamp}] High Network Traffic - PID: {pid}, Name: {name}, "
                                 f"Sent: {sent_delta} bytes, Received: {received_delta} bytes")
                    log_entries.append(log_entry)
                    print(log_entry.strip())  # Print to the console

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        # Update the previous traffic snapshot
        previous_traffic = current_traffic

        time.sleep(1)  # Poll every 1 second for a quick snapshot

    # Return the log as a string after the timeout
    return "\n".join(log_entries)

if __name__ == "__main__":
    log_output = monitor_network_traffic(timeout=5)
    print("Monitoring completed. Log output:")
    print(log_output)

