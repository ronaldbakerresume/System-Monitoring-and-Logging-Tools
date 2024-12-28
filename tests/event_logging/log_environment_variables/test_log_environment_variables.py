import unittest
from unittest.mock import patch, MagicMock
import psutil
from src.event_logging.log_environment_variables.log_env_logger import log_environment_variables

class TestLogEnvironmentVariables(unittest.TestCase):
    @patch("psutil.process_iter")
    def test_log_environment_variables(self, mock_process_iter):
        """
        Test that log_environment_variables returns the correct formatted string for mock processes.
        """
        # Mock process details
        mock_process1 = MagicMock()
        mock_process1.info = {"pid": 1234, "name": "nginx"}
        mock_process1.environ.return_value = {"PATH": "/usr/bin", "USER": "root"}

        mock_process2 = MagicMock()
        mock_process2.info = {"pid": 5678, "name": "mysql"}
        mock_process2.environ.return_value = {"PATH": "/usr/sbin", "USER": "mysql"}

        # Set the return value of psutil.process_iter
        mock_process_iter.return_value = [mock_process1, mock_process2]

        # Call the function
        log_output = log_environment_variables()

        # Assertions
        self.assertIn("Process: PID 1234, Name: nginx", log_output)
        self.assertIn("  PATH=/usr/bin", log_output)
        self.assertIn("  USER=root", log_output)
        self.assertIn("Process: PID 5678, Name: mysql", log_output)
        self.assertIn("  PATH=/usr/sbin", log_output)
        self.assertIn("  USER=mysql", log_output)

    @patch("psutil.process_iter")
    def test_handle_no_process(self, mock_process_iter):
        """
        Test that the function handles no processes correctly.
        """
        mock_process_iter.return_value = []
        log_output = log_environment_variables()
        self.assertNotIn("Process:", log_output)

    @patch("psutil.process_iter")
    def test_skip_inaccessible_processes(self, mock_process_iter):
        """
        Test that inaccessible processes are skipped without error.
        """
        mock_process1 = MagicMock()
        mock_process1.info = {"pid": 1234, "name": "nginx"}
        mock_process1.environ.side_effect = psutil.AccessDenied  # Simulate inaccessible process

        mock_process_iter.return_value = [mock_process1]

        log_output = log_environment_variables()
        self.assertNotIn("nginx", log_output)  # No entry for nginx because it's inaccessible

if __name__ == "__main__":
    unittest.main()

