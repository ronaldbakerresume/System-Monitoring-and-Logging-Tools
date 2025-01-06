import unittest
from unittest.mock import patch, MagicMock
from src.process_logging.log_excessive_file_descriptors import log_excessive_file_descriptors

class TestLogExcessiveFileDescriptors(unittest.TestCase):
    @patch("src.process_logging.log_excessive_file_descriptors.psutil.process_iter")
    def test_log_excessive_file_descriptors(self, mock_process_iter):
        # Mock process behavior
        mock_proc1 = MagicMock()
        mock_proc1.info = {"pid": 123, "name": "Process1"}
        mock_proc1.open_files.return_value = [MagicMock()] * 150  # 150 file descriptors

        mock_proc2 = MagicMock()
        mock_proc2.info = {"pid": 456, "name": "Process2"}
        mock_proc2.open_files.return_value = [MagicMock()] * 50  # 50 file descriptors

        # Simulate psutil.process_iter returning processes
        mock_process_iter.return_value = [mock_proc1, mock_proc2]

        # Run the function for a short duration
        log_output = log_excessive_file_descriptors(duration_seconds=5, polling_interval=1)

        # Assertions
        self.assertIn("Excessive File Descriptors Detected", log_output)
        self.assertIn("PID: 123", log_output)
        self.assertIn("Name: Process1", log_output)
        self.assertNotIn("PID: 456", log_output)  # Process2 should not appear in the log

if __name__ == "__main__":
    unittest.main()
