import os
import shutil

def bring_python_projects_to_top():
    """
    Moves all Python scripts from subdirectories to the top level of the current working directory.
    If a directory contains only one script, clones and renames the README file if it exists.
    """
    source_dir = os.getcwd()  # Automatically set the source directory to the current working directory

    # List all subdirectories and files in the source directory
    for root, dirs, files in os.walk(source_dir, topdown=False):
        for file in files:
            if file.endswith(".py"):  # Only process Python files
                file_path = os.path.join(root, file)

                # If there's a README.md file in the same directory, rename and clone it
                if len(files) == 1 and "README.md" in files:
                    readme_path = os.path.join(root, "README.md")
                    new_readme_name = f"README_{os.path.splitext(file)[0]}.md"
                    new_readme_path = os.path.join(source_dir, new_readme_name)
                    shutil.copy(readme_path, new_readme_path)
                    print(f"Cloned README to: {new_readme_path}")

                # Move the Python script to the top level
                new_path = os.path.join(source_dir, file)
                shutil.move(file_path, new_path)
                print(f"Moved {file} to: {new_path}")

        # If the directory becomes empty after moving files, remove it
        if not os.listdir(root) and root != source_dir:
            os.rmdir(root)
            print(f"Removed empty directory: {root}")

# Run the script
if __name__ == "__main__":
    bring_python_projects_to_top()

