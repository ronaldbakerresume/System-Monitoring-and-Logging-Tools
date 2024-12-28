import os
import ast
import importlib

def is_python_package(directory):
    """
    Determines if a directory is a Python package by checking for __init__.py.
    """
    return os.path.isfile(os.path.join(directory, "__init__.py"))

def verify_imports(project_dir):
    """
    Verifies imports recursively, starting from the top-level directory.
    It follows the Python directory structure (packages and subpackages).

    :param project_dir: Path to the top-level directory of the project.
    """
    for root, _, files in os.walk(project_dir):
        if not is_python_package(root) and root != project_dir:
            # Skip non-package directories unless it's the project root
            continue

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Checking imports in: {file_path}")
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        tree = ast.parse(f.read(), filename=file_path)
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Import):
                                for alias in node.names:
                                    verify_single_import(alias.name, file_path)
                            elif isinstance(node, ast.ImportFrom):
                                module = node.module or ""
                                verify_single_import(module, file_path, from_import=True)
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")

def verify_single_import(module_name, file_path, from_import=False):
    """
    Verifies a single import statement.

    :param module_name: Name of the module being imported.
    :param file_path: Path to the file containing the import.
    :param from_import: Whether this is a "from ... import ..." statement.
    """
    try:
        importlib.import_module(module_name)
        print(f"  ✅ {module_name}")
    except ModuleNotFoundError as e:
        error_type = "from import" if from_import else "import"
        print(f"  ❌ Invalid {error_type}: {module_name} in {file_path} ({e})")
    except ImportError as e:
        print(f"  ⚠️ Import error for {module_name} in {file_path}: {e}")

if __name__ == "__main__":
    # Get the current working directory (assumes script is run from the top-level project directory)
    project_directory = os.getcwd()  # Start from the current directory
    verify_imports(project_directory)

