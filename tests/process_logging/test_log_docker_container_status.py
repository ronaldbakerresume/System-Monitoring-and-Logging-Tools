import unittest
from unittest.mock import patch
import subprocess  # Import subprocess to resolve NameError
from src.process_logging.log_docker_container_status import log_docker_container_status

class TestLogDockerContainerStatus(unittest.TestCase):
    @patch("subprocess.run")
    def test_log_docker_container_status(self, mock_subprocess_run):
        # Mock subprocess.run to simulate Docker ps output
        mock_subprocess_run.return_value = unittest.mock.Mock(
            stdout="1234567,example_container_1,Up 5 minutes\n7654321,example_container_2,Exited (0) 2 hours ago",
            returncode=0
        )

        # Call the function
        result = log_docker_container_status()

        # Check if the log contains expected entries
        self.assertIn("1234567,example_container_1,Up 5 minutes", result)
        self.assertIn("7654321,example_container_2,Exited (0) 2 hours ago", result)

    @patch("subprocess.run", side_effect=FileNotFoundError)
    def test_docker_not_found(self, mock_subprocess_run):
        # Simulate Docker command not found
        result = log_docker_container_status()

        # Check for the specific error message
        self.assertIn("Error: Docker command not found", result)

    @patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "docker ps"))
    def test_docker_command_error(self, mock_subprocess_run):
        # Simulate a Docker command error
        result = log_docker_container_status()

        # Check for the error handling message
        self.assertIn("An error occurred while fetching Docker statuses", result)

if __name__ == "__main__":
    unittest.main()

