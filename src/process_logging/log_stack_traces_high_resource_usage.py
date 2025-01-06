import os
import psutil
from datetime import datetime


def log_stack_traces_high_resource_usage(cpu_threshold=50.0, memory_threshold_mb=500, log_file="high_resource_usage_stack_traces_log.txt"):
    """
    Logs processes consuming excessive resources and their stack traces.

    Args:
        cpu_threshold (float): CPU usage percentage threshold.
        memory_threshold_mb (float): Memory usage threshold in MB.
        log_file (str): Path to the log file.

    Returns:
        str: Formatted string output of logged processes and their stack traces.
    """
    log_output = []
    header = f"High Resource Usage Stack Trace Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n" + "=" * 60 + "\n"
    log_output.append(header)

    for process in psutil.process_iter(attrs=["pid", "name", "cpu_percent", "memory_info"]):
        try:
            pid = process.info["pid"]
            name = process.info["name"]
            cpu_usage = process.info["cpu_percent"]
            memory_usage_mb = process.info["memory_info"].rss / (1024 * 1024)  # Convert to MB

            if cpu_usage > cpu_threshold or memory_usage_mb > memory_threshold_mb:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_entry = (f"[{timestamp}] High Resource Usage Process - PID: {pid}, "
                             f"Name: {name}, CPU: {cpu_usage:.2f}%, "
                             f"Memory: {memory_usage_mb:.2f} MB\n")
                log_output.append(log_entry)

                try:
                    stack_trace = f"Stack Trace for PID {pid}:\n(Not implemented in Python for running processes)\n"
                    log_output.append(stack_trace)
                except Exception as stack_error:
                    error_entry = f"Error capturing stack trace for PID {pid}: {stack_error}\n"
                    log_output.append(error_entry)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    log_output.append("\n")

    # Write to file
    with open(log_file, "w") as file:
        file.write("".join(log_output))

    return "".join(log_output)


if __name__ == "__main__":
    output = log_stack_traces_high_resource_usage()
    print(output)
