import unittest
from unittest.mock import patch, MagicMock
from src.process_logging.log_hardware_interactions import log_hardware_interactions

class TestLogHardwareInteractions(unittest.TestCase):
    @patch("src.process_logging.log_hardware_interactions.psutil.net_connections")
    @patch("src.process_logging.log_hardware_interactions.psutil.Process")
    def test_log_hardware_interactions(self, mock_process, mock_net_connections):
        # Mock network connections
        mock_conn1 = MagicMock()
        mock_conn1.laddr = MagicMock(ip="127.0.0.1", port=8080)
        mock_conn1.raddr = MagicMock(ip="192.168.1.1", port=80)
        mock_conn1.status = "ESTABLISHED"
        mock_conn1.pid = 1234

        mock_conn2 = MagicMock()
        mock_conn2.laddr = MagicMock(ip="10.0.0.1", port=22)
        mock_conn2.raddr = None  # No remote address
        mock_conn2.status = "LISTEN"
        mock_conn2.pid = 5678

        mock_net_connections.return_value = [mock_conn1, mock_conn2]

        # Mock process details
        mock_proc1 = MagicMock()
        mock_proc1.name.return_value = "MockProcess1"
        mock_proc2 = MagicMock()
        mock_proc2.name.return_value = "MockProcess2"

        mock_process.side_effect = lambda pid: mock_proc1 if pid == 1234 else mock_proc2

        # Run the function for a short duration
        log_output = log_hardware_interactions(duration_seconds=5, log_file="test_hardware_log.txt")

        # Assertions
        self.assertIn("PID 1234", log_output)
        self.assertIn("Name: MockProcess1", log_output)
        self.assertIn("Local Address: 127.0.0.1:8080", log_output)
        self.assertIn("Remote Address: 192.168.1.1:80", log_output)
        self.assertIn("Status: ESTABLISHED", log_output)

        self.assertIn("PID 5678", log_output)
        self.assertIn("Name: MockProcess2", log_output)
        self.assertIn("Local Address: 10.0.0.1:22", log_output)
        self.assertIn("Remote Address: N/A", log_output)
        self.assertIn("Status: LISTEN", log_output)

if __name__ == "__main__":
    unittest.main()
