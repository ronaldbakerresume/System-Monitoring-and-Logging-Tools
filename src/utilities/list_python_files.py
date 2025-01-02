import os

def list_python_files_from_parent():
    """
    Recursively lists all Python files from the parent directory.

    :return: A list of tuples containing file names and their absolute paths.
    """
    parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    python_files = []
    
    for root, _, files in os.walk(parent_directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                python_files.append((file, file_path))
    
    return python_files

if __name__ == "__main__":
    python_files = list_python_files_from_parent()
    
    if python_files:
        print("\nPython files found in the parent directory and subdirectories:")
        for file_name, file_path in python_files:
            print(f"File: {file_name}, Path: {file_path}")
    else:
        print("\nNo Python files found in the parent directory.")

