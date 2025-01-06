import psutil
from datetime import datetime


def log_unauthorized_execution(
    authorized_directories=None, poll_interval=5, log_file="unauthorized_execution_log.txt"
):
    """
    Monitors and logs processes executing from unauthorized directories.

    Args:
        authorized_directories (list): List of directories considered authorized.
        poll_interval (int): Time in seconds between monitoring cycles.
        log_file (str): Path to the log file.

    Returns:
        str: Formatted string output of unauthorized execution logs.
    """
    if authorized_directories is None:
        authorized_directories = ["/usr/bin", "/bin", "C:\\Windows\\System32", "/usr/sbin"]

    log_output = []
    header = f"Unauthorized Execution Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n" + "=" * 60 + "\n"
    log_output.append(header)

    try:
        for process in psutil.process_iter(attrs=["pid", "name", "exe"]):
            try:
                pid = process.info["pid"]
                name = process.info["name"]
                exe_path = process.info.get("exe", "N/A")

                if exe_path != "N/A" and not any(exe_path.startswith(auth_dir) for auth_dir in authorized_directories):
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = (f"[{timestamp}] Unauthorized Execution Detected - "
                                 f"PID: {pid}, Name: {name}, Executable Path: {exe_path}\n")
                    log_output.append(log_entry)

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    except Exception as e:
        log_output.append(f"An error occurred: {e}\n")

    # Write to log file
    with open(log_file, "w") as file:
        file.write("".join(log_output))

    return "".join(log_output)


if __name__ == "__main__":
    output = log_unauthorized_execution()
    print(output)
