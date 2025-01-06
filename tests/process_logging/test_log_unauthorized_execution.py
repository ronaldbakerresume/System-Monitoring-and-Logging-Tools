import unittest
from unittest.mock import patch, MagicMock
from src.process_logging.log_unauthorized_execution import log_unauthorized_execution


class TestLogUnauthorizedExecution(unittest.TestCase):
    @patch("src.process_logging.log_unauthorized_execution.psutil.process_iter")
    def test_unauthorized_execution_logging(self, mock_process_iter):
        # Mock process data
        mock_process_1 = MagicMock()
        mock_process_1.info = {"pid": 1234, "name": "test_process_1", "exe": "/usr/bin/test_process"}

        mock_process_2 = MagicMock()
        mock_process_2.info = {"pid": 5678, "name": "test_process_2", "exe": "/unauthorized/path/test_process"}

        mock_process_3 = MagicMock()
        mock_process_3.info = {"pid": 91011, "name": "test_process_3", "exe": "N/A"}  # Invalid path

        mock_process_iter.return_value = [mock_process_1, mock_process_2, mock_process_3]

        # Run the function
        log_output = log_unauthorized_execution(
            authorized_directories=["/usr/bin", "/bin"]
        )

        # Assertions
        self.assertIn("Unauthorized Execution Detected - PID: 5678", log_output)
        self.assertIn("Executable Path: /unauthorized/path/test_process", log_output)
        self.assertNotIn("Unauthorized Execution Detected - PID: 1234", log_output)  # Authorized
        self.assertNotIn("Executable Path: N/A", log_output)  # Invalid path

        # Ensure the output has a timestamp header
        self.assertIn("Unauthorized Execution Log", log_output)


if __name__ == "__main__":
    unittest.main()
