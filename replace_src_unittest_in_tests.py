import os

def replace_src_unittest_in_tests(test_dir):
    """
    Recursively replaces all occurrences of 'src.unittest' with 'unittest' in test files.

    :param test_dir: Path to the root of the test directory.
    """
    for root, _, files in os.walk(test_dir):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Replace 'src.unittest' with 'unittest'
                updated_content = content.replace("src.unittest", "unittest")

                if content != updated_content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(updated_content)
                    print(f"  Updated: {file_path}")
                else:
                    print(f"  No changes needed for: {file_path}")

if __name__ == "__main__":
    test_directory = "tests"  # Replace with the path to your test directory
    replace_src_unittest_in_tests(test_directory)

