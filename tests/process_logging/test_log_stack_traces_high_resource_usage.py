import unittest
from unittest.mock import patch, MagicMock
from src.process_logging.log_stack_traces_high_resource_usage import log_stack_traces_high_resource_usage


class TestLogStackTracesHighResourceUsage(unittest.TestCase):
    @patch("src.process_logging.log_stack_traces_high_resource_usage.psutil.process_iter")
    def test_log_stack_traces(self, mock_process_iter):
        # Mock process data
        mock_process_1 = MagicMock()
        mock_process_1.info = {
            "pid": 1234,
            "name": "test_process_1",
            "cpu_percent": 60.0,
            "memory_info": MagicMock(rss=600 * 1024 * 1024)  # 600 MB
        }

        mock_process_2 = MagicMock()
        mock_process_2.info = {
            "pid": 5678,
            "name": "test_process_2",
            "cpu_percent": 30.0,
            "memory_info": MagicMock(rss=200 * 1024 * 1024)  # 200 MB
        }

        mock_process_iter.return_value = [mock_process_1, mock_process_2]

        # Run the function
        log_output = log_stack_traces_high_resource_usage(cpu_threshold=50.0, memory_threshold_mb=500)

        # Assertions
        self.assertIn("High Resource Usage Process - PID: 1234", log_output)
        self.assertIn("CPU: 60.00%", log_output)
        self.assertIn("Memory: 600.00 MB", log_output)
        self.assertNotIn("High Resource Usage Process - PID: 5678", log_output)  # Below threshold

        # Ensure the stack trace placeholder is in the output
        self.assertIn("Stack Trace for PID 1234:", log_output)


if __name__ == "__main__":
    unittest.main()
