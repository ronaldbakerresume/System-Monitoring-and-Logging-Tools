import os

def ensure_init_files(test_dir):
    """
    Ensures an __init__.py file exists in every directory under the given test directory.

    :param test_dir: Path to the root of the test directory.
    """
    for root, _, files in os.walk(test_dir):
        # Skip if __init__.py already exists
        init_file = os.path.join(root, "__init__.py")
        if "__init__.py" not in files:
            try:
                with open(init_file, "w", encoding="utf-8") as f:
                    f.write("# This file marks the directory as a package for Python testing.\n")
                print(f"Created: {init_file}")
            except Exception as e:
                print(f"Error creating {init_file}: {e}")
        else:
            print(f"Already exists: {init_file}")

if __name__ == "__main__":
    # Set the path to your test directory
    test_directory = "tests"  # Replace with the path to your test directory
    ensure_init_files(test_directory)

