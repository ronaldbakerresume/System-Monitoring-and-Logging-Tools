import unittest
from unittest.mock import patch
from src.network_monitoring.log_listening_processes import log_listening_processes  # Corrected import

class TestLogListeningProcesses(unittest.TestCase):
    @patch("subprocess.run")
    def test_log_listening_processes(self, mock_subprocess_run):
        # Mock the subprocess output for testing
        mock_subprocess_run.return_value.stdout = (
            "Proto Local Address           Foreign Address         State\n"
            "tcp   0.0.0.0:80             0.0.0.0:*               LISTEN\n"
            "tcp   0.0.0.0:22             0.0.0.0:*               LISTEN\n"
            "tcp   127.0.0.1:443          0.0.0.0:*               LISTEN\n"
        )

        # Call the function and get the output
        output = log_listening_processes()

        # Assert that the monitored ports appear in the output
        self.assertIn(":80", output)
        self.assertIn(":22", output)
        self.assertIn(":443", output)

    @patch("subprocess.run")
    def test_no_matching_ports(self, mock_subprocess_run):
        # Mock the subprocess output with no matching ports
        mock_subprocess_run.return_value.stdout = (
            "Proto Local Address           Foreign Address         State\n"
            "tcp   0.0.0.0:12345          0.0.0.0:*               LISTEN\n"
        )

        # Call the function and get the output
        output = log_listening_processes()

        # Assert that no monitored ports appear in the output
        self.assertNotIn(":80", output)
        self.assertNotIn(":22", output)
        self.assertNotIn(":443", output)

if __name__ == "__main__":
    unittest.main()
