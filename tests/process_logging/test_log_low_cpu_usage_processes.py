import unittest
from unittest.mock import patch, MagicMock
from src.process_logging.log_low_cpu_usage_processes import log_low_cpu_usage_processes

class TestLogLowCPUUsageProcesses(unittest.TestCase):
    @patch("src.process_logging.log_low_cpu_usage_processes.psutil.process_iter")
    def test_low_cpu_usage_logging(self, mock_process_iter):
        # Mock processes
        mock_process1 = MagicMock()
        mock_process1.info = {"pid": 1234, "name": "Process1", "cpu_percent": 0.5}
        
        mock_process2 = MagicMock()
        mock_process2.info = {"pid": 5678, "name": "Process2", "cpu_percent": 1.5}

        mock_process_iter.return_value = [mock_process1, mock_process2]

        # Run the function with mocked data
        log_output = log_low_cpu_usage_processes(duration_seconds=5, polling_interval=1, log_file="test_low_cpu_log.txt")

        # Assertions
        self.assertIn("PID: 1234", log_output)
        self.assertIn("Name: Process1", log_output)
        self.assertIn("CPU Usage: 0.50%", log_output)

        # Ensure the second process is not logged as it exceeds the threshold
        self.assertNotIn("PID: 5678", log_output)

if __name__ == "__main__":
    unittest.main()
