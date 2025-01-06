import unittest
from unittest.mock import patch, MagicMock
from src.process_logging.log_cpu_affinity_violations import log_cpu_affinity_violations

class TestLogCpuAffinityViolations(unittest.TestCase):
    @patch("psutil.process_iter")
    def test_log_cpu_affinity_violations(self, mock_process_iter):
        # Mock process data
        mock_process_1 = MagicMock()
        mock_process_1.info = {"pid": 123, "name": "example_process_1"}
        mock_process_1.cpu_affinity.return_value = [2, 3]  # Not matching expected

        mock_process_2 = MagicMock()
        mock_process_2.info = {"pid": 456, "name": "example_process_2"}
        mock_process_2.cpu_affinity.return_value = [2, 3]  # Matching expected

        mock_process_iter.return_value = [mock_process_1, mock_process_2]

        # Run the function
        result = log_cpu_affinity_violations()

        # Assert output
        self.assertIn("CPU Affinity Violation - PID: 123, Name: example_process_1", result)
        self.assertNotIn("CPU Affinity Violation - PID: 456, Name: example_process_2", result)

if __name__ == "__main__":
    unittest.main()