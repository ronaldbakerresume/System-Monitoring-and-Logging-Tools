```markdown
# System Monitoring and Logging Tools

This repository contains a collection of Python scripts for monitoring, logging, and managing various system activities. Each script resides in its dedicated directory, with a detailed `README.md` file explaining its functionality, usage, and configuration.

## Directory Overview

Below is a list of all script directories, along with a brief description of their functionality. Click on each directory name to navigate to its detailed `README.md` file.

### Detection Scripts

- [**detect_runaway_processes/**](detect_runaway_processes/): Detects processes that exceed a specified runtime threshold.
- [**detect_unauthorized_executables/**](detect_unauthorized_executables/): Identifies processes using unauthorized executables or scripts.

### Logging Scripts

- [**log_config_file_modifications/**](log_config_file_modifications/): Logs attempts to modify critical system configuration files.
- [**log_cpu_affinity_violations/**](log_cpu_affinity_violations/): Tracks and logs processes violating CPU core affinity rules.
- [**log_critical_directory_access/**](log_critical_directory_access/): Logs processes accessing critical directories like `/etc` or `/home`.
- [**log_critical_file_deletion/**](log_critical_file_deletion/): Detects and logs attempts to delete critical system files.
- [**log_docker_container_status/**](log_docker_container_status/): Logs the statuses of running Docker containers.
- [**log_environment_variables/**](log_environment_variables/): Logs the environment variables of monitored processes.
- [**log_excessive_child_processes/**](log_excessive_child_processes/): Tracks and logs processes spawning an excessive number of child processes.
- [**log_excessive_file_descriptors/**](log_excessive_file_descriptors/): Logs processes with a high number of open file descriptors.
- [**log_excessive_memory_usage/**](log_excessive_memory_usage/): Logs processes consuming excessive memory.
- [**log_file_locking_processes/**](log_file_locking_processes/): Logs processes holding locks on specific files.
- [**log_frequent_process_restarts/**](log_frequent_process_restarts/): Detects processes restarting frequently within a given time window.
- [**log_gpu_resource_usage/**](log_gpu_resource_usage/): Tracks and logs processes consuming GPU resources.
- [**log_hardware_interactions/**](log_hardware_interactions/): Logs processes interacting with hardware devices such as USB or network interfaces.
- [**log_high_thread_count/**](log_high_thread_count/): Logs processes with high thread counts.
- [**log_interprocess_signals/**](log_interprocess_signals/): Tracks and logs inter-process communication signals.
- [**log_kernel_module_access/**](log_kernel_module_access/): Logs processes accessing or interacting with kernel modules or drivers.
- [**log_listening_processes/**](log_listening_processes/): Logs processes listening on specific network ports.
- [**log_low_cpu_usage_processes/**](log_low_cpu_usage_processes/): Logs processes with unusually low CPU usage over time.
- [**log_open_file_descriptors/**](log_open_file_descriptors/): Logs open file descriptors for processes.
- [**log_priority_changes/**](log_priority_changes/): Tracks and logs changes in scheduling priority for processes.
- [**log_privilege_escalation_attempts/**](log_privilege_escalation_attempts/): Detects and logs unauthorized privilege escalation attempts.
- [**log_privileged_port_bindings/**](log_privileged_port_bindings/): Logs processes attempting to bind to privileged ports (<1024).
- [**log_privileged_processes/**](log_privileged_processes/): Monitors and logs processes running with elevated privileges.
- [**log_process_count_changes/**](log_process_count_changes/): Tracks and logs changes in the total number of running processes.
- [**log_process_hierarchy/**](log_process_hierarchy/): Logs parent-child relationships of active processes.
- [**log_running_processes/**](log_running_processes/): Logs metadata (e.g., PID, name, command) for all currently running processes.
- [**log_shared_memory_processes/**](log_shared_memory_processes/): Tracks and logs processes using shared memory.
- [**log_specific_network_access/**](log_specific_network_access/): Monitors and logs processes accessing specific IP addresses or domains.
- [**log_stack_traces_high_resource_usage/**](log_stack_traces_high_resource_usage/): Captures and logs stack traces for processes with high resource usage.
- [**log_temp_file_disk_usage/**](log_temp_file_disk_usage/): Tracks disk usage by processes writing to temporary files.
- [**log_top_cpu_processes/**](log_top_cpu_processes/): Continuously logs the top 10 CPU-consuming processes.
- [**log_unauthorized_execution/**](log_unauthorized_execution/): Detects processes executing from unauthorized directories.

### Monitoring Tools

- [**monitor_child_processes/**](monitor_child_processes/): Monitors child processes spawned by a specific parent process.
- [**monitor_command_line_arguments/**](monitor_command_line_arguments/): Monitors command-line arguments of processes for suspicious activity.
- [**monitor_critical_processes/**](monitor_critical_processes/): Tracks critical system processes and logs failures or terminations.
- [**monitor_device_filesystem_writes/**](monitor_device_filesystem_writes/): Logs processes writing to specific devices or filesystems.
- [**monitor_disk_io_processes/**](monitor_disk_io_processes/): Tracks and logs processes with high disk I/O usage.
- [**monitor_file_access/**](monitor_file_access/): Logs processes accessing specific files or directories.
- [**monitor_high_cpu_processes/**](monitor_high_cpu_processes/): Logs processes with high CPU usage.
- [**monitor_network_traffic/**](monitor_network_traffic/): Tracks and logs processes with high network traffic.
- [**monitor_unauthorized_processes/**](monitor_unauthorized_processes/): Logs processes not on an authorized process list.
- [**monitor_virtual_memory_usage/**](monitor_virtual_memory_usage/): Logs processes consuming significant amounts of virtual memory.

### Utility Scripts

- [**organize_files_with_readme/**](organize_files_with_readme/): Organizes files into subdirectories with auto-generated `README.md` files.

## How to Use

- Navigate to the directory of interest.
- Read the `README.md` file for detailed usage instructions.
- Run the Python script provided in the directory.

---

Secure, monitor, and optimize your system with these scripts! 🚀
```
```
