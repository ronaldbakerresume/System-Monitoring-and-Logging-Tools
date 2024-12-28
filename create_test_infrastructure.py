import os

def create_test_infrastructure(source_dir, test_dir):
    """
    Creates a testing infrastructure for the given source directory.
    Generates a test script for each Python module with a stencil test function.
    
    :param source_dir: Path to the source directory containing Python modules.
    :param test_dir: Path to the directory where test scripts should be created.
    """
    for root, dirs, files in os.walk(source_dir):
        # Calculate relative path from source_dir
        relative_path = os.path.relpath(root, source_dir)
        test_subdir = os.path.join(test_dir, relative_path)

        # Create corresponding subdirectory in test_dir
        os.makedirs(test_subdir, exist_ok=True)

        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                # Determine module name and corresponding test file path
                module_name = os.path.splitext(file)[0]
                test_file = os.path.join(test_subdir, f"test_{module_name}.py")

                # Generate test script content
                test_script_content = f"""
import unittest
from {relative_path.replace(os.sep, '.')} import {module_name}

class Test{module_name.capitalize()}(unittest.TestCase):
    def test_example(self):
        # Placeholder test for {module_name}
        self.assertTrue(True)  # Replace with actual test logic

if __name__ == "__main__":
    unittest.main()
"""

                # Write the test script to the test directory
                with open(test_file, "w") as f:
                    f.write(test_script_content.strip())

    print(f"Test infrastructure created in '{test_dir}'.")

# Example Usage
if __name__ == "__main__":
    source_directory = "src"  # Replace with the path to your source directory
    test_directory = "tests"  # Replace with the path to your test directory
    create_test_infrastructure(source_directory, test_directory)

