#!/bin/bash

# Script: organize_files_with_readme.sh
# Developer: Ronald Baker
# Purpose: Organizes files in the current directory by placing each file into its own subdirectory and adding a README.md file.
# Compatible with: Linux, macOS, and Windows (via WSL)

# Use the current directory as the source directory
SOURCE_DIR="$(pwd)"

# README.md template
README_TEMPLATE="# File Information

This directory contains the following file:
- '%s'

Organized automatically with 'organize_files_with_readme.sh'.
"

# Function to organize files
organize_files_with_readme() {
    # Iterate over all files in the source directory
    for file in "$SOURCE_DIR"/*; do
        if [[ -f "$file" ]]; then
            # Get the file name and extension
            filename=$(basename "$file")
            base_name="${filename%.*}"

            # Create a subdirectory for the file
            subdirectory="$SOURCE_DIR/$base_name"
            mkdir -p "$subdirectory"

            # Move the file into the new subdirectory
            mv "$file" "$subdirectory/"

            # Create the README.md file in the new subdirectory
            readme_path="$subdirectory/README.md"
            printf "$README_TEMPLATE" "$filename" > "$readme_path"

            echo "Organized file '$filename' into '$subdirectory' with README.md."
        fi
    done

    echo "All files have been organized successfully."
}

# Run the function
organize_files_with_readme

