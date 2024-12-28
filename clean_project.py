import os
import shutil

def clean_project(root_dir="."):
    """
    Cleans up unnecessary files and directories in a Python project.
    :param root_dir: The root directory of the project (default is current directory).
    """
    extensions_to_delete = [".pyc", ".pyo", ".log", ".tmp", ".bak"]
    directories_to_delete = ["__pycache__", "build", "dist", "*.egg-info", "env", "venv"]

    for root, dirs, files in os.walk(root_dir):
        # Delete files with specific extensions
        for file in files:
            if any(file.endswith(ext) for ext in extensions_to_delete):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

        # Delete specific directories
        for dir_name in dirs:
            if dir_name in directories_to_delete or dir_name.endswith(".egg-info"):
                dir_path = os.path.join(root, dir_name)
                shutil.rmtree(dir_path, ignore_errors=True)
                print(f"Deleted directory: {dir_path}")

if __name__ == "__main__":
    clean_project()

