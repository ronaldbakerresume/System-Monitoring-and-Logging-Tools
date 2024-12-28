import os

def rename_test_files_with_prefix(directory, prefix="NOT_TESTED_"):
    """
    Renames all files starting with 'test_' by adding the prefix 'NOT_TESTED_'.

    :param directory: Path to the root directory containing test files.
    :param prefix: Prefix to add to the test file names (default: "NOT_TESTED_").
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, prefix + file)
                
                if not file.startswith(prefix):  # Avoid re-renaming already prefixed files
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")
                else:
                    print(f"Already renamed: {old_path}")

if __name__ == "__main__":
    # Replace 'tests' with the path to your test directory
    test_directory = "tests"  # Adjust as needed
    rename_test_files_with_prefix(test_directory)

