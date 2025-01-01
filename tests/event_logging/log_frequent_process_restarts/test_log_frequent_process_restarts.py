import unittest
from datetime import datetime, timedelta
from src.event_logging.log_frequent_process_restarts import log_freq_process_restarts

class TestLogFrequentProcessRestarts(unittest.TestCase):
    def test_no_restarts(self):
        simulated_processes = [
            {"pid": 1, "name": "process1", "create_time": datetime.now() - timedelta(seconds=70)},
            {"pid": 2, "name": "process2", "create_time": datetime.now() - timedelta(seconds=50)},
        ]
        result = log_frequent_process_restarts(simulated_processes=simulated_processes)
        self.assertEqual(result, "No frequent restarts detected.")

    def test_frequent_restarts(self):
        now = datetime.now()
        simulated_processes = [
            {"pid": 1, "name": "process1", "create_time": now - timedelta(seconds=50)},
            {"pid": 1, "name": "process1", "create_time": now - timedelta(seconds=30)},
            {"pid": 1, "name": "process1", "create_time": now - timedelta(seconds=10)},
            {"pid": 1, "name": "process1", "create_time": now},
        ]
        result = log_frequent_process_restarts(simulated_processes=simulated_processes)
        self.assertIn("Frequent Restarts Detected", result)
        self.assertIn("PID: 1", result)

    def test_partial_restarts(self):
        now = datetime.now()
        simulated_processes = [
            {"pid": 1, "name": "process1", "create_time": now - timedelta(seconds=120)},
            {"pid": 1, "name": "process1", "create_time": now - timedelta(seconds=60)},
            {"pid": 1, "name": "process1", "create_time": now},
        ]
        result = log_frequent_process_restarts(simulated_processes=simulated_processes)
        self.assertEqual(result, "No frequent restarts detected.")

if __name__ == "__main__":
    unittest.main()
