import os
import shutil

def copy_python_files_to_top_level():
    """
    Copies all Python files from subdirectories to the top-level directory.
    """
    current_dir = os.getcwd()
    top_level_files = []

    for root, _, files in os.walk(current_dir):
        for file in files:
            if file.endswith(".py") and root != current_dir:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(current_dir, file)

                # Avoid overwriting files with the same name
                if os.path.exists(destination_path):
                    base, ext = os.path.splitext(file)
                    count = 1
                    while os.path.exists(destination_path):
                        destination_path = os.path.join(current_dir, f"{base}_{count}{ext}")
                        count += 1

                # Copy the file
                shutil.copy2(source_path, destination_path)
                top_level_files.append(destination_path)
                print(f"Copied: {source_path} -> {destination_path}")

    if not top_level_files:
        print("No Python files found in subdirectories.")
    else:
        print("\nAll Python files have been copied to the top-level directory.")

if __name__ == "__main__":
    copy_python_files_to_top_level()

