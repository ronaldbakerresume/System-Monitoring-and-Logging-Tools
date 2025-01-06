import unittest
from unittest.mock import patch, MagicMock
from src.process_logging.log_running_processes import log_running_processes


class TestLogRunningProcesses(unittest.TestCase):
    @patch("src.process_logging.log_running_processes.subprocess.run")
    @patch("src.process_logging.log_running_processes.os.name", new_callable=lambda: "posix")
    def test_log_running_processes(self, mock_subprocess_run):
        # Mock subprocess output for a Linux/MacOS system
        mock_result = MagicMock()
        mock_result.stdout = "PID   COMMAND         ARGS\n123   python3         script.py\n456   bash            -c sleep"
        mock_subprocess_run.return_value = mock_result

        # Run the function
        log_output = log_running_processes(log_file="test_running_processes_log.txt")

        # Assertions on the returned text
        self.assertIn("Process Log -", log_output)
        self.assertIn("PID   COMMAND         ARGS", log_output)
        self.assertIn("123   python3         script.py", log_output)
        self.assertIn("456   bash            -c sleep", log_output)

    @patch("src.process_logging.log_running_processes.subprocess.run")
    @patch("src.process_logging.log_running_processes.os.name", new_callable=lambda: "nt")
    def test_log_running_processes_windows(self, mock_subprocess_run):
        # Mock subprocess output for a Windows system
        mock_result = MagicMock()
        mock_result.stdout = "Image Name                     PID Session Name        Session#    Mem Usage\npython.exe                    1234 Console                    1     15,000 K"
        mock_subprocess_run.return_value = mock_result

        # Run the function
        log_output = log_running_processes(log_file="test_running_processes_log_windows.txt")

        # Assertions on the returned text
        self.assertIn("Process Log -", log_output)
        self.assertIn("Image Name                     PID Session Name", log_output)
        self.assertIn("python.exe                    1234", log_output)


if __name__ == "__main__":
    unittest.main()
