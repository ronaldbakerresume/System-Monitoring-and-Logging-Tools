import os
import re

def add_src_prefix_to_imports(test_dir):
    """
    Recursively adds "src." to module imports in test files if not already present.

    :param test_dir: Path to the directory containing test files.
    """
    for root, _, files in os.walk(test_dir):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")

                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                updated_lines = []
                modified = False

                for line in lines:
                    # Match 'from module import ...' or 'import module'
                    match = re.match(r"^(from|import) (\w+(\.\w+)*)(\s+import\s+.*)?", line)
                    if match:
                        import_type, module_name, _, rest = match.groups()

                        # Add "src." if not already present
                        if not module_name.startswith("src."):
                            updated_line = f"{import_type} src.{module_name}{rest or ''}\n"
                            updated_lines.append(updated_line)
                            modified = True
                            print(f"  Updated: {line.strip()} -> {updated_line.strip()}")
                        else:
                            updated_lines.append(line)
                    else:
                        updated_lines.append(line)

                # Write changes back to the file if modified
                if modified:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.writelines(updated_lines)
                    print(f"  Changes applied to: {file_path}")
                else:
                    print(f"  No changes needed for: {file_path}")

if __name__ == "__main__":
    test_directory = "tests"  # Replace with the path to your test directory
    add_src_prefix_to_imports(test_directory)

