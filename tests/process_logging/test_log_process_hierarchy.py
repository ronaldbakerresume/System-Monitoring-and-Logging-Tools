import unittest
from unittest.mock import patch, MagicMock
from src.process_logging.log_process_hierarchy import log_process_hierarchy


class TestLogProcessHierarchy(unittest.TestCase):
    @patch("src.process_logging.log_process_hierarchy.psutil.process_iter")
    @patch("src.process_logging.log_process_hierarchy.psutil.Process")
    def test_log_process_hierarchy(self, mock_process, mock_process_iter):
        # Mock parent process
        mock_parent = MagicMock()
        mock_parent.name.return_value = "ParentProcess"

        # Mock child processes
        mock_process1 = MagicMock()
        mock_process1.info = {"pid": 1234, "name": "ChildProcess1", "ppid": 5678}

        mock_process2 = MagicMock()
        mock_process2.info = {"pid": 4321, "name": "ChildProcess2", "ppid": 5678}

        # Mock psutil behaviors
        mock_process_iter.return_value = [mock_process1, mock_process2]
        mock_process.return_value = mock_parent

        # Run the function
        log_output = log_process_hierarchy(log_file="test_process_hierarchy_log.txt")

        # Assertions on the returned text
        self.assertIn("Process: PID 1234, Name: ChildProcess1 --> Parent: PID 5678, Name: ParentProcess", log_output)
        self.assertIn("Process: PID 4321, Name: ChildProcess2 --> Parent: PID 5678, Name: ParentProcess", log_output)

        # Verify that the header is included
        self.assertIn("Process Hierarchy Log", log_output)
        self.assertIn("=" * 60, log_output)


if __name__ == "__main__":
    unittest.main()
