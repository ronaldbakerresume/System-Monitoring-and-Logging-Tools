import unittest
from unittest.mock import patch, MagicMock
from src.process_logging.log_excessive_child_processes import log_excessive_child_processes

class TestLogExcessiveChildProcesses(unittest.TestCase):
    @patch("src.process_logging.log_excessive_child_processes.psutil.process_iter")
    @patch("src.process_logging.log_excessive_child_processes.psutil.Process")
    def test_log_excessive_child_processes(self, mock_process, mock_process_iter):
        # Mock process behavior
        mock_proc1 = MagicMock()
        mock_proc1.info = {"pid": 1, "name": "Process1"}
        mock_proc1.children.return_value = [MagicMock()] * 12  # 12 child processes

        mock_proc2 = MagicMock()
        mock_proc2.info = {"pid": 2, "name": "Process2"}
        mock_proc2.children.return_value = [MagicMock()] * 5  # 5 child processes (below threshold)

        # Simulate psutil.process_iter returning a list of processes
        mock_process_iter.return_value = [mock_proc1, mock_proc2]

        # Run the function with a short duration for testing
        log_output = log_excessive_child_processes(duration_seconds=5, polling_interval=1)

        # Assertions
        self.assertIn("Excessive Child Processes Detected", log_output)
        self.assertIn("PID: 1", log_output)
        self.assertIn("Name: Process1", log_output)
        self.assertNotIn("PID: 2", log_output)  # Process2 should not be logged

if __name__ == "__main__":
    unittest.main()
