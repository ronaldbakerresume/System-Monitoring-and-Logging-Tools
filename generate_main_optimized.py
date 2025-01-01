#!/usr/bin/env python3

"""
Script to dynamically collect and generate imports from the src directory, avoiding redundant submodule imports.
Author: Mavericks Umbrella LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import pkgutil

def discover_top_level_imports(directory):
    """
    Dynamically discovers Python modules and packages in the src directory, filtering out submodules.

    Args:
        directory (str): The root directory to scan for src.

    Returns:
        set: A set of unique top-level import statements.
    """
    src_path = os.path.join(directory, "src")
    if not os.path.isdir(src_path):
        print(f"No 'src' directory found in: {directory}")
        return set()

    imports = set()
    all_modules = set()

    # Collect all discovered modules and submodules
    for finder, name, is_pkg in pkgutil.walk_packages([src_path], prefix="src."):
        all_modules.add(name)

    # Filter submodules: Keep only the top-level modules
    for module in all_modules:
        if not any(module.startswith(parent + ".") for parent in all_modules):
            imports.add(f"import {module}")

    return imports

def create_main_file(imports, output_file="main.py"):
    """
    Creates a main.py file with the discovered imports and an application header.

    Args:
        imports (set): A set of Python import statements.
        output_file (str): The name of the main file to create.
    """
    header = f"""#!/usr/bin/env python3

\"\"\"
Auto-generated main.py file.
Author: Mavericks Umbrella LLC

This file includes dynamically discovered Python modules from the src directory.
Redundant submodule imports have been removed for clarity.
Feel free to customize it as needed.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
\"\"\"

print("Welcome to the application!")
print("This script automatically imports the following modules:")
"""

    with open(output_file, "w") as f:
        # Write header
        f.write(header)
        
        # Write imports
        for imp in sorted(imports):
            f.write(f"{imp}\n")
        
        f.write("\nif __name__ == '__main__':\n")
        f.write("    print('Application setup complete. Add your main application logic here!')\n")
    
    print(f"main.py has been created with {len(imports)} imports.")

def main():
    current_dir = os.getcwd()
    print(f"Scanning for Python modules in the 'src' directory under: {current_dir}")

    imports = discover_top_level_imports(current_dir)
    if imports:
        print("\nDiscovered Top-Level Imports:")
        for imp in sorted(imports):
            print(imp)
        
        create_main_file(imports)
    else:
        print("No Python modules or packages found in the 'src' directory, or the directory does not exist.")

if __name__ == "__main__":
    main()

