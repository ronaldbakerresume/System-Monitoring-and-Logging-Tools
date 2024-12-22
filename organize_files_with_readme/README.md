
# organize_files_with_readme.sh

A Bash script designed to organize files in the current directory by creating individual subdirectories for each file and automatically generating a corresponding `README.md` file for each.

## Features

- **Automatic Organization**: Each file is moved into a subdirectory named after the file (excluding the extension).
- **README.md Generation**: A `README.md` file is created in each subdirectory, documenting the file contained within.
- **Cross-Platform Compatibility**: Compatible with Linux, macOS, and Windows (via WSL).

## How It Works

The script performs the following steps:
1. Iterates over all files in the current directory.
2. For each file:
   - Creates a subdirectory named after the file (excluding the extension).
   - Moves the file into the new subdirectory.
   - Generates a `README.md` file in the subdirectory with the file details.

## Usage

1. Clone or copy the script to your system.
2. Make the script executable:
   ```bash
   chmod +x organize_files_with_readme.sh
   ```
3. Run the script in the directory you want to organize:
   ```bash
   ./organize_files_with_readme.sh
   ```
4. The script will organize all files in the current directory.

## Example

**Before Running:**
```
/my_directory
    file1.txt
    file2.pdf
    image.jpg
```

**After Running:**
```
/my_directory
    /file1
        file1.txt
        README.md
    /file2
        file2.pdf
        README.md
    /image
        image.jpg
        README.md
```

Each `README.md` will contain:
```markdown
# File Information

This directory contains the following file:
- 'file1.txt'

Organized automatically with 'organize_files_with_readme.sh'.
```

## Dependencies

- Bash shell
- Compatible operating system:
  - Linux
  - macOS
  - Windows Subsystem for Linux (WSL)

## Customization

You can modify the `README_TEMPLATE` variable in the script to customize the content of the generated `README.md` files. For example, you could add additional metadata or formatting.

## Author

**Ronald Baker**  
A developer passionate about automating repetitive tasks and enhancing productivity through simple yet effective tools.

## License

This script is licensed under the [MIT License](LICENSE), which permits reuse, modification, and distribution.

---

Happy organizing! 🚀
```

Feel free to let me know if you'd like any additional sections or modifications!
