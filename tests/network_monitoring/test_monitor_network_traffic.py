import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from src.network_monitoring.monitor_network_traffic import monitor_network_traffic

class TestMonitorNetworkTraffic(unittest.TestCase):
    @patch("psutil.net_connections")
    @patch("psutil.Process")
    def test_high_network_traffic(self, mock_process, mock_net_connections):
        # Mock psutil.net_connections to simulate network connections
        mock_connection = MagicMock()
        mock_connection.pid = 1234
        mock_connection.laddr = ("127.0.0.1", 8080)
        mock_connection.raddr = ("0.0.0.0", 0)
        mock_net_connections.return_value = [mock_connection]

        # Mock the Process object to simulate the process traffic
        mock_process.return_value.io_counters.return_value = MagicMock(
            other_bytes_sent=1024 * 1024 * 2, other_bytes_recv=1024 * 1024 * 3
        )

        # Mock the current time for consistent timestamping in the test
        fixed_timestamp = datetime(2025, 1, 1, 12, 0, 0)

        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value = fixed_timestamp
            # Call the monitor function with a 5-second timeout
            output = monitor_network_traffic(timeout=5)

        # Assert that the log contains expected information without hardcoding the timestamp
        self.assertIn("High Network Traffic Log -", output)  # Check if log header is present
        self.assertIn("PID: 1234", output)
        self.assertIn("Sent: 2097152 bytes", output)  # 2 MB sent
        self.assertIn("Received: 3145728 bytes", output)  # 3 MB received
        self.assertIn(f"High Network Traffic Log - {fixed_timestamp.strftime('%Y-%m-%d %H:%M:%S')}", output)

    @patch("psutil.net_connections")
    @patch("psutil.Process")
    def test_no_high_network_traffic(self, mock_process, mock_net_connections):
        # Mock psutil.net_connections to simulate network connections
        mock_connection = MagicMock()
        mock_connection.pid = 5678
        mock_connection.laddr = ("127.0.0.1", 80)
        mock_connection.raddr = ("0.0.0.0", 0)
        mock_net_connections.return_value = [mock_connection]

        # Mock the Process object to simulate the process traffic
        mock_process.return_value.io_counters.return_value = MagicMock(
            other_bytes_sent=1024 * 1024, other_bytes_recv=1024 * 1024
        )

        # Mock the current time for consistent timestamping in the test
        fixed_timestamp = datetime(2025, 1, 1, 12, 0, 0)

        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value = fixed_timestamp
            # Call the monitor function with a 5-second timeout
            output = monitor_network_traffic(timeout=5)

        # Assert that no high traffic log entries are present
        self.assertIn("High Network Traffic Log -", output)  # Check if log header is present
        self.assertNotIn("High Network Traffic", output)  # Check if no high traffic entry is logged
        self.assertIn(f"High Network Traffic Log - {fixed_timestamp.strftime('%Y-%m-%d %H:%M:%S')}", output)

    @patch("psutil.net_connections")
    def test_no_matching_ports(self, mock_net_connections):
        # Simulate a process listening on a non-matching port
        mock_connection = MagicMock()
        mock_connection.pid = 1234
        mock_connection.laddr = ("127.0.0.1", 8081)  # Non-matching port
        mock_connection.raddr = ("0.0.0.0", 0)
        mock_net_connections.return_value = [mock_connection]

        # Mock the current time for consistent timestamping in the test
        fixed_timestamp = datetime(2025, 1, 1, 12, 0, 0)

        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value = fixed_timestamp
            # Call the monitor function for logging listening processes
            output = monitor_network_traffic(timeout=5)

        # Assert that ":22" is not found in the log if port 22 is excluded by filter
        self.assertNotIn(":22", output)

if __name__ == "__main__":
    unittest.main()
