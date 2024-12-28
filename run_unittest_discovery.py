import unittest

def run_unittest_discovery():
    """
    Runs the equivalent of 'python -m unittest discover -s tests -p "test_*.py"'.
    """
    # Create a test loader and discover tests
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="test_*.py")
    
    # Create a test runner to execute the suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    run_unittest_discovery()

