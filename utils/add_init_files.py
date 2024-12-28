import os

def add_init_files(test_dir):
    """
    Adds an __init__.py file to each directory containing test files.

    :param test_dir: Path to the root of the testing framework (e.g., 'tests/').
    """
    for root, dirs, files in os.walk(test_dir):
        # Check if the directory contains any test files
        test_files = [file for file in files if file.startswith("test_") and file.endswith(".py")]
        if test_files:
            init_file_path = os.path.join(root, "__init__.py")
            # Create __init__.py if it doesn't exist
            if not os.path.exists(init_file_path):
                with open(init_file_path, "w") as f:
                    f.write("# This file makes the directory a package for unittest discovery.\n")
                print(f"Created: {init_file_path}")
            else:
                print(f"Already exists: {init_file_path}")

# Example Usage
if __name__ == "__main__":
    test_directory = "tests"  # Replace with the path to your test directory
    add_init_files(test_directory)

